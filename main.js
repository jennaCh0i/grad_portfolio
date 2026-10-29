// Contact links — fill these in once and every Email / LinkedIn / Resume link on the page updates.
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

// Project filters
const chips = [...document.querySelectorAll(".chip[data-filter]")];
const cards = [...document.querySelectorAll(".card[data-tags]")];

function applyFilter(filter) {
  chips.forEach((chip) => {
    const active = chip.dataset.filter === filter;
    chip.classList.toggle("is-active", active);
    chip.setAttribute("aria-pressed", String(active));
  });
  cards.forEach((card) => {
    const show = filter === "all" || card.dataset.tags.split(" ").includes(filter);
    card.hidden = !show;
  });
}

chips.forEach((chip) => chip.addEventListener("click", () => applyFilter(chip.dataset.filter)));

// "Work ▾" menu items jump to the grid and apply a filter
document.querySelectorAll("[data-filter-link]").forEach((link) => {
  link.addEventListener("click", () => {
    applyFilter(link.dataset.filterLink);
    link.closest("details")?.removeAttribute("open");
  });
});

// Only one header menu open at a time; close on outside click / Escape
const menus = [...document.querySelectorAll("details.menu")];
menus.forEach((menu) =>
  menu.addEventListener("toggle", () => {
    if (menu.open) menus.forEach((m) => m !== menu && m.removeAttribute("open"));
  })
);
document.addEventListener("click", (e) => {
  menus.forEach((m) => !m.contains(e.target) && m.removeAttribute("open"));
});
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") menus.forEach((m) => m.removeAttribute("open"));
});
