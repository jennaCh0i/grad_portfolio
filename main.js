// Contact links — fill these in once and every Email / LinkedIn / Résumé link on the site updates.
const LINKS = {
  email: "",    // e.g. "hello@jennachoi.work"
  linkedin: "", // e.g. "https://www.linkedin.com/in/your-handle"
  resume: "",   // e.g. "/assets/Jenna_Choi_Resume.pdf"
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
