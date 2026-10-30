// One-off: collect images, videos and text from the old Cargo site.
import { chromium } from "playwright";
import fs from "node:fs/promises";

const BASE = "https://jennachoi.work";
const PAGES = ["", "hermes", "wired-1", "sweetie", "campertwins", "all-life-alive",
  "petersen-automotive-museum", "about-me", "playground"];

const out = { pages: {} };
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1600, height: 1000 } });

let netUrls = new Set();
page.on("request", (req) => {
  const u = req.url();
  if (/freight\.cargo\.site|vimeo|\.mp4|\.webm/.test(u)) netUrls.add(u);
});

for (const slug of PAGES) {
  const url = `${BASE}/${slug}`;
  netUrls = new Set();
  try {
    await page.goto(url, { waitUntil: "load", timeout: 90000 });
    await page.waitForTimeout(3000);
    for (let i = 0; i < 40; i++) { await page.mouse.wheel(0, 1200); await page.waitForTimeout(250); }
    await page.waitForTimeout(1500);
    const data = await page.evaluate(() => {
      const urls = new Set();
      const all = [];
      const walk = (root) => root.querySelectorAll("*").forEach((el) => { all.push(el); if (el.shadowRoot) walk(el.shadowRoot); });
      walk(document);
      document.querySelectorAll("img").forEach((i) => {
        [i.currentSrc, i.src, i.dataset.src].forEach((u) => u && urls.add(u));
        (i.srcset || "").split(",").forEach((p) => { const u = p.trim().split(" ")[0]; if (u) urls.add(u); });
      });
      all.filter((e) => e.tagName === "IMG").forEach((i) => {
        [i.currentSrc, i.src].forEach((u) => u && urls.add(u));
      });
      all.forEach((el) => {
        const bg = getComputedStyle(el).backgroundImage;
        (bg.match(/url\(["']?([^"')]+)["']?\)/g) || []).forEach((m) => urls.add(m.replace(/url\(["']?|["']?\)/g, "")));
      });
      const videos = all.filter((e) => e.tagName === "VIDEO" || e.tagName === "SOURCE").map((v) => v.currentSrc || v.src).filter(Boolean);
      const iframes = all.filter((e) => e.tagName === "IFRAME").map((f) => f.src).filter(Boolean);
      return { images: [...urls], videos, iframes, text: document.body.innerText };
    });
    netUrls.forEach((u) => (/\.(mp4|webm|mov)/i.test(u) ? data.videos : data.images).push(u));
    data.images = [...new Set(data.images)];
    data.videos = [...new Set(data.videos)];
    out.pages[slug || "home"] = data;
    console.log(slug || "home", data.images.length, "images", data.videos.length, "videos", data.iframes.length, "iframes");
  } catch (e) {
    console.log("FAILED", url, e.message);
  }
}
await browser.close();

// Download originals of every Cargo image (dedup by hash)
await fs.mkdir("cargo-import/images", { recursive: true });
const seen = new Map();
for (const [slug, d] of Object.entries(out.pages)) {
  d.files = [];
  for (const u of [...d.images, ...d.videos]) {
    const m = u.match(/freight\.cargo\.site\/.*?\/i\/([A-Za-z0-9]+)\/([^?#]+)/);
    if (!m) continue;
    const [, hash, name] = m;
    const file = `${slug}__${decodeURIComponent(name).replace(/[^\w.\-]+/g, "_")}`;
    if (!seen.has(hash)) {
      const orig = `https://freight.cargo.site/t/original/i/${hash}/${name}`;
      for (const src of [orig, u]) {
        try {
          const r = await fetch(src);
          if (!r.ok) continue;
          await fs.writeFile(`cargo-import/images/${file}`, Buffer.from(await r.arrayBuffer()));
          seen.set(hash, file);
          break;
        } catch {}
      }
    }
    if (seen.has(hash)) d.files.push(seen.get(hash));
  }
  await fs.writeFile(`cargo-import/${slug}.txt`, d.text);
  delete d.text;
}
await fs.writeFile("cargo-import/manifest.json", JSON.stringify(out, null, 2));
console.log("downloaded", seen.size, "files");
