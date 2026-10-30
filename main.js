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

// Project filters (with counts)
const chips = [...document.querySelectorAll(".chip[data-filter]")];
const cards = [...document.querySelectorAll(".card[data-tags]")];

chips.forEach((chip) => {
  const f = chip.dataset.filter;
  const n = f === "all" ? cards.length : cards.filter((c) => c.dataset.tags.split(" ").includes(f)).length;
  const count = document.createElement("span");
  count.className = "chip__count";
  count.textContent = n;
  chip.append(count);
});

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

// Grid / List view toggle
const grid = document.querySelector(".grid");
const viewBtns = [...document.querySelectorAll("[data-view]")];
function setView(view) {
  if (!grid) return;
  grid.classList.toggle("is-list", view === "list");
  viewBtns.forEach((b) => {
    const on = b.dataset.view === view;
    b.classList.toggle("is-active", on);
    b.setAttribute("aria-pressed", String(on));
  });
  try { localStorage.setItem("view", view); } catch (e) {}
}
viewBtns.forEach((b) => b.addEventListener("click", () => setView(b.dataset.view)));
try { if (localStorage.getItem("view") === "list") setView("list"); } catch (e) {}
