# Jenna Choi — portfolio

Static site (plain HTML / CSS / JS, no build step), deployed on Vercel from `main`.

Every page is **generated**: edit the text, cards and media lists in `tools/content.py`, then run
`python3 tools/build_site.py`. That writes `index.html`, `about.html`, `fun.html` and the project pages
(`hermes`, `wired`, `sweetie`, `camper`, `all-life-alive`, `petersen`).
- `styles.css` — tokens, layout, components
- `main.js` — work filters, live clock, contact links (`LINKS` at the top)
- `assets/work/` — home thumbnails · `assets/projects/<slug>/` — project images (`NN.webp`) and loops (`vNN.mp4`)

Originals imported from the old Cargo site live on the `cargo-import` branch.

Run locally: `npx serve .`
