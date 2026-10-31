# Jenna Choi — portfolio

Static site (plain HTML / CSS / JS, no build step), deployed on Vercel from `main`.

- `index.html` — Work (project grid + filters)
- `about.html`, `fun.html` — About and Fun pages
- `hermes.html`, `wired.html`, `sweetie.html`, `camper.html`, `all-life-alive.html`, `petersen.html`
  — project pages, **generated** by `tools/build_projects.py`. Edit the text/media list there and run
  `python3 tools/build_projects.py`.
- `styles.css` — tokens, layout, components
- `main.js` — filters, Grid/List view, "On this page" highlighting, contact links (`LINKS` at the top)
- `assets/work/` — home thumbnails · `assets/projects/<slug>/` — project images (`NN.webp`) and loops (`vNN.mp4`)

Originals imported from the old Cargo site live on the `cargo-import` branch.

Run locally: `npx serve .`
