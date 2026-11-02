// Contact links — fill these in once and every Email / LinkedIn / Résumé link on the site updates.
const LINKS = {
  email: "jennachoi814@gmail.com",
  linkedin: "https://www.linkedin.com/in/jenna-choi-558182250/",
  resume: "/assets/Jenna_Choi_Resume.pdf",
};

document.querySelectorAll("[data-link]").forEach((el) => {
  const value = LINKS[el.dataset.link];
  if (!value) return;
  el.href = el.dataset.link === "email" ? `mailto:${value}` : value;
});

// Live local time, e.g. "Pasadena. 5:17:02 PM"
document.querySelectorAll("[data-clock]").forEach((el) => {
  const fmt = new Intl.DateTimeFormat("en-US", {
    timeZone: el.dataset.tz || undefined,
    hour: "numeric",
    minute: "2-digit",
    second: "2-digit",
  });
  const tick = () => { el.textContent = `${el.dataset.city}. ${fmt.format(new Date())}`; };
  tick();
  setInterval(tick, 1000);
});

// Work filters (home), with project counts
const filterBtns = [...document.querySelectorAll("[data-filter]")];
const cards = [...document.querySelectorAll(".card[data-tags]")];
const matches = (card, f) => f === "all" || card.dataset.tags.split(" ").includes(f);

filterBtns.forEach((btn) => {
  const count = document.createElement("span");
  count.className = "chip__count";
  count.textContent = cards.filter((c) => matches(c, btn.dataset.filter)).length;
  btn.append(count);
  btn.addEventListener("click", () => {
    const f = btn.dataset.filter;
    filterBtns.forEach((b) => {
      const on = b === btn;
      b.classList.toggle("is-active", on);
      b.setAttribute("aria-pressed", String(on));
    });
    cards.forEach((c) => { c.hidden = !matches(c, f); });
  });
});

// Card videos that only play on hover (or while on screen, on touch devices)
const hoverVideos = [...document.querySelectorAll("video[data-hover-play]")];
const canHover = window.matchMedia("(hover: hover)").matches;
const play = (v) => { v.preload = "auto"; v.play().catch(() => {}); };
const stop = (v) => { v.pause(); v.currentTime = v.closest(".fig") ? 0.1 : 0; };
if (canHover) {
  hoverVideos.forEach((v) => {
    const card = v.closest(".card, .fig") || v;
    card.addEventListener("mouseenter", () => play(v));
    card.addEventListener("mouseleave", () => stop(v));
    card.addEventListener("focusin", () => play(v));
    card.addEventListener("focusout", () => stop(v));
  });
} else if ("IntersectionObserver" in window) {
  const io = new IntersectionObserver((entries) =>
    entries.forEach((e) => (e.isIntersecting ? play(e.target) : stop(e.target))), { threshold: 0.6 });
  hoverVideos.forEach((v) => io.observe(v));
}

// Project pages: highlight the section you're reading in the left shortcuts
const sectionLinks = [...document.querySelectorAll("[data-section]")];
if (sectionLinks.length && "IntersectionObserver" in window) {
  const targets = sectionLinks.map((a) => document.getElementById(a.dataset.section)).filter(Boolean);
  const mark = (id) => sectionLinks.forEach((a) => a.classList.toggle("is-here", a.dataset.section === id));
  const io = new IntersectionObserver((entries) => {
    const hit = entries.filter((e) => e.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
    if (hit) mark(hit.target.id);
  }, { rootMargin: "-15% 0px -70% 0px" });
  targets.forEach((t) => io.observe(t));
  mark(targets[0] && targets[0].id);
  // at the very bottom, highlight the last section
  window.addEventListener("scroll", () => {
    if (window.innerHeight + window.scrollY >= document.body.scrollHeight - 4) mark(targets[targets.length - 1].id);
  }, { passive: true });
}
