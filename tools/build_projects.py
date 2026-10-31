"""Generate the project pages (hermes.html, wired.html, ...) from the data below.

Run from the repo root:  python3 tools/build_projects.py
Media references:
  "i:08"            -> assets/projects/<slug>/08.webp (or .gif)
  "v:01"            -> assets/projects/<slug>/v01.mp4 (autoplay, muted, loop)
  "vimeo:1234"      -> Vimeo player
  "iframe:<url>"    -> embedded page
A row is a list of 1-4 items; (item, "caption") pairs add a caption.
"""
import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECTS = [
    {
        "slug": "hermes",
        "card": "Hermes Sponsored Project",
        "meta": "Hermès Sponsored Project · 2D/3D Motion Graphics + Visual · 2025",
        "title": "Vivlio book holder — Your Imaginary World, In Your Pocket",
        "summary": "Access your personal escape wherever you are. Whether tucked in a book, slipped into a pocket, or packed in your bag, the Vivlio book holder brings comfort within reach—on a yacht, in the sky, or from the couch.",
        "hero": "vimeo:1107782299",
        "facts": [("Role", "Graphic Designer<br>Motion Designer"), ("Timeline", "10 weeks"),
                  ("Tools", "Cinema 4D<br>After Effects<br>Illustrator"), ("Recognition", "Core77")],
        "deliverables": [
            "Led the visual design across product developing a distinct color palette and custom illustrations",
            "Shaped the core storytelling through a mix of 2D and 3D design",
            "Built a functional design system in close collaboration with industrial designers",
            "Managed the design team and kept the creative process focused and efficient",
            "Worked hands-on with industrial designers to bring the product vision to life",
            "Designed the final window display and presentation to showcase the full experience",
        ],
        "sections": [
            {"id": "renders", "nav": "Renders", "label": "Key renders",
             "body": "Designed for comfort, going beyond function into the realm of the imaginary with Vivlio Hermès. New product integrated with existing product.",
             "rows": [["i:08"], ["i:09"]]},
            {"id": "detail", "nav": None, "label": "Detail renders", "rows": [["i:07"], ["i:10"]]},
            {"id": "color", "nav": "Color", "label": "Color & illustration",
             "body": "Developing a distinct color palette and custom illustrations.",
             "rows": [["i:03", "i:04"], ["i:05", "i:06"], ["i:11", "i:12"], ["i:13", "i:14", "i:15"]]},
            {"id": "display", "nav": "Display", "label": "Window display",
             "body": "Honoring the process of craftsmanship — the window display and presentation showcase the full experience.",
             "link": ("See the project day ↗", "https://www.linkedin.com/posts/jenna-choi-558182250_hermestalents-pasadena-artcentercollegeofdesign-activity-7323772498284576768-7gMl"),
             "rows": [["i:01", "i:02"], ["i:00"]]},
            {"id": "storytelling", "nav": "Storytelling", "label": "Storytelling",
             "body": "Storytelling through a mix of 2D and 3D design.",
             "rows": [["vimeo:1016915690"]]},
            {"id": "moments", "nav": None, "label": "Key moments", "rows": [["i:16"]]},
        ],
    },
    {
        "slug": "wired",
        "card": "WIRED logo reveal",
        "meta": "3D Motion Graphics · 2024",
        "title": "WIRED Logo Animation",
        "summary": "WIRED is where tomorrow is realized— new ways of thinking, new connections, and new industries.",
        "note": "*Student project, not affiliated with the company.",
        "hero": "vimeo:1032615423",
        "facts": [("Category", "3D Motion Graphics"), ("Year", "2024"), ("Tools", "Cinema 4D")],
        "deliverables": [
            "Led the visual design across product developing a distinct color palette and custom illustrations",
            "Shaped the core storytelling through a mix of 2D and 3D design",
        ],
        "sections": [
            {"id": "renders", "nav": "Key renders", "label": "Key renders",
             "body": "WIRED is where tomorrow is realized— new ways of thinking, new connections, and new industries.",
             "rows": [[("v:01", "Foundation material of WIRED"), ("v:02", "Shape. Sculpt. Mold")],
                      [("v:03", "Innovation. Development"), ("v:04", "Evolving and transforming into NEW")],
                      [("v:05", "Integrating new technologies"), ("i:05", "Logo Lock-Up")]]},
            {"id": "process", "nav": "Process", "label": "Process",
             "body": "Using Cinema 4D, soft body dynamics were explored, gravity was utilized, and material nodes were customized. The process also involved multiple passes of pre-rendering and adjustments.",
             "rows": [["v:06", "v:07"], [("i:08", "Initial sketching for logo animation")]]},
        ],
    },
    {
        "slug": "sweetie",
        "card": "Customize your salad, Sweetie AI",
        "meta": "UI/UX · AI · Motion · 2026",
        "title": "Sweetie — Start with one word",
        "summary": "Sweetie is an AI-powered ordering experience for Sweetgreen that turns a single word — a craving, a mood, or a need — into a strong starting bowl, so customers never have to build one from scratch.",
        "note": "*Student project, not affiliated with Sweetgreen.",
        "hero": "i:00",
        "facts": [("Role", "UI designer"), ("Timeline", "10 weeks"), ("Tools", "Figma")],
        "sections": [
            {"id": "problem", "nav": "Problem", "label": "Problem",
             "heading": "Too much customization can turn choice into decision overload.",
             "body": "Today’s ordering flow asks customers to build every bowl ingredient by ingredient.",
             "rows": [[("i:12", "Current Sweetgreen in-store kiosk")]]},
            {"id": "audience", "nav": None, "label": "Who is this for?",
             "body": "Customers who know what they want, but not exactly what to order — people in a hurry, new to the menu, working toward a dietary goal, or looking for a personalized bowl without building it from scratch.",
             "facts": [("Top task", "Get a personalized bowl recommendation from a single keyword."),
                       ("Sub tasks", "Review the recommended bowl<br>Understand why the bowl was recommended<br>Check ingredients and nutrition<br>Explore ingredient sourcing<br>Customize the recommendation if needed")]},
            {"id": "prototype", "nav": "Prototype", "label": "Try the prototype",
             "body": "Interactive tablet prototype — click through it here, or open it full size.",
             "link": ("Open in new tab ↗", "https://jennach0i.github.io/sweetie-design-system/app/"),
             "rows": [["iframe:https://jennach0i.github.io/sweetie-design-system/app/?record"]]},
            {"id": "experience", "nav": "Experience", "label": "Experience",
             "body": "An information architecture built around one keyword, with the LLM stepping in at the moments that need judgement.",
             "flow": ["Keyword", "Recommendation", "Customize", "Order", "Understand"],
             "rows": [[("v:01", "01 — Start with a keyword. Start with one word."), ("v:02", "Suggested keywords and what others are ordering.")],
                      [("v:03", "02 — Recommendation & customize. Adjust bases, toppings and dressings, then order."), ("i:07", "Refreshing · High protein · 620 cal")],
                      [("v:04", "03 — Ask & learn your ingredients."), ("v:05", "04 — Your orders. Reorder a favorite or revisit what was in your bowl.")]]},
            {"id": "micro", "nav": "Micro-interactions", "label": "Micro-interactions",
             "body": "Small, soft motions that show the AI is working and confirm every choice.",
             "rows": [[("v:06", "Trending nudge — pops out of the Sweetie button when there’s something to explore."),
                       ("v:07", "Store header — location and hours slide in so you know where you’re ordering."),
                       ("v:08", "Keyword wheel — keywords scroll into focus and blur as they leave.")],
                      [("v:09", "Bowl ready — the hex breathes while the bowl is being built."),
                       ("v:10", "Ingredient amounts — pills fill to show how much, and stop at the group limit."),
                       ("v:11", "Dietary toggles — filters snap on with a check, so the choice is confirmed.")]]},
            {"id": "system", "nav": "Design system", "label": "Design system",
             "facts": [("Fresh", "Starts from what the user wants right now — their mood, craving, goal, or preference."),
                       ("Curated", "Thoughtfully selects and combines ingredients into a personalized recommendation."),
                       ("Real", "Builds trust by showing real nutrition, ingredients, and sourcing behind the recommendation.")],
             "rows": [[("i:10", "Fresh · Curated · Real")],
                      [("i:08", "Figtree Regular"), ("i:09", "Dark Green #00473D · Sweetie Gradient · Greys, Light Green, Beige")],
                      [("i:13", "1px outline · 30px corner radius · hex bowl"), ("i:11", "Brand identity")]]},
        ],
    },
    {
        "slug": "camper",
        "card": "Camper Twin Campaign",
        "meta": "Campaign · Motion Graphics",
        "title": "Camper Twin Campaign — What is Twin?",
        "summary": "While twins share a bond, they aren’t always identical. It’s more than looking alike—it’s the special connection that makes them belong together. This campaign celebrates how Camper shoes, like twins, might be different in details but are always made to be side by side, bringing out the best in each other.",
        "hero": "vimeo:1050423228",
        "facts": [("Project type", "Motion Graphics"), ("Software", "After Effects<br>Illustrator")],
        "sections": [
            {"id": "moments", "nav": "Key moments", "label": "Key moments",
             "rows": [[("v:01", "Same flower different in shape."), ("v:02", "Different usage, same form language.")],
                      [("v:03", "Symbiotic relationships."), ("i:01", "Twins can be in various forms.")],
                      [("v:05", "When twins are together they create a harmony."), ("v:06", "Camper Twins. They are the ONE.")]]},
            {"id": "icon", "nav": "Icon", "label": "A Camper’s icon",
             "body": "TWINS — subtly mismatched but perfectly compatible.", "rows": [["i:04"]]},
            {"id": "process", "nav": "Process", "label": "Process",
             "rows": [[("i:05", "Using After Effects to adjust keyframes and get the timing right"),
                       ("i:06", "Using Illustrator to custom illustrate the style of Camper’s unique identity")],
                      [("i:07", "Final process before it turned to animation")]]},
        ],
    },
    {
        "slug": "all-life-alive",
        "card": "MIT LIST ArtCenter: All Life Alive",
        "meta": "Wayfinding + Visual Communication · 2024",
        "title": "MIT List Visual Arts Center — All Life Alive",
        "summary": "MIT List Visual Arts Center’s exhibition presents a cutting-edge exploration of bioart, where the works examine the intersections of biology, technology, and identity.",
        "note": "*Student project, not affiliated with MIT List Visual Arts Center.",
        "hero": "vimeo:995925121",
        "facts": [("Category", "Wayfinding + Visual Communication"), ("Year", "2024")],
        "deliverables": [
            "Led the visual design across product developing a distinct color palette and custom illustrations",
            "Shaped the core storytelling through a mix of 2D and 3D design",
        ],
        "sections": [
            {"id": "wayfinding", "nav": "Wayfinding", "label": "Wayfinding system",
             "body": "Maps and signages welcome visitors, immersing them in the experience prior to the exhibition.",
             "rows": [["i:07"], ["i:08"], ["i:09"]]},
            {"id": "exhibition", "nav": "Exhibition", "label": "Exhibition space",
             "body": "The space is designed to reflect each artist’s unique style while maximizing its space.",
             "rows": [["i:10"], ["i:06", "i:00"]]},
            {"id": "catalogue", "nav": "Catalogue", "label": "Exhibition catalogue",
             "rows": [["i:01", "i:02"], ["i:03"], ["i:04", "i:05"]]},
        ],
    },
    {
        "slug": "petersen",
        "card": "Petersen Automotive Museum",
        "meta": "Rebranding · Brand Identity",
        "title": "Petersen Automotive Museum Rebrand",
        "summary": "The Petersen Automotive Museum is an automobile museum located on Wilshire Boulevard alongside Museum Row in the Miracle Mile neighborhood of Los Angeles. One of the world’s largest collections, the Petersen Automotive Museum is a nonprofit organization specializing in automobile history and related educational programs.",
        "hero": "i:14",
        "facts": [("Project type", "Rebranding / Brand Identity"), ("Software", "InDesign<br>Illustrator<br>After Effects<br>C4D")],
        "sections": [
            {"id": "mission", "nav": None, "label": "Mission",
             "heading": "Petersen Automotive Museum’s new gear shift. Redefining the drive, igniting the momentum.",
             "rows": [["v:02"]]},
            {"id": "identity", "nav": "Brand identity", "label": "Brand identity",
             "rows": [[("i:21", "Momentum — feel the speed and time"), ("i:22", "Persona — unique personalities and stories")],
                      [("i:23", "Gem — treasure our exclusive collection"), ("i:24", "Shift — our gear shifting innovation")],
                      ["i:03"], ["i:02"], ["i:01"]]},
            {"id": "logo", "nav": "Logo & system", "label": "Logo & brand system",
             "rows": [["i:12", "i:13"], ["v:01"], ["i:15"], ["i:16"], ["i:17"], ["i:19"]]},
            {"id": "color", "nav": "Color & type", "label": "Color / typography system",
             "body": "The Petersen Automotive Museum chose colors to evoke speed, movement, and passion associated with automobiles.",
             "rows": [["i:00"]]},
            {"id": "ideation", "nav": "Ideation", "label": "Brandscape & mindmap",
             "rows": [["i:04", "i:05"], ["i:06"], ["i:07"], ["i:08", "i:09"], ["i:10", "i:11"]]},
        ],
    },
]


def esc(s):
    return html.escape(s, quote=True)


def asset(slug, ref):
    kind, val = ref.split(":", 1)
    base = f"/assets/projects/{slug}"
    if kind == "i":
        ext = "gif" if os.path.exists(os.path.join(ROOT, f"assets/projects/{slug}/{val}.gif")) else "webp"
        return f'<img src="{base}/{val}.{ext}" alt="" loading="lazy" decoding="async" />'
    if kind == "v":
        return f'<video src="{base}/v{val}.mp4" autoplay muted loop playsinline preload="metadata"></video>'
    if kind == "vimeo":
        return (f'<div class="embed"><iframe src="https://player.vimeo.com/video/{val}?title=0&byline=0&portrait=0&dnt=1" '
                f'allow="autoplay; fullscreen; picture-in-picture" allowfullscreen loading="lazy" title="Video"></iframe></div>')
    if kind == "iframe":
        return f'<div class="embed embed--app"><iframe src="{esc(val)}" loading="lazy" title="Prototype"></iframe></div>'
    raise ValueError(ref)


def media(slug, item):
    ref, cap = item if isinstance(item, tuple) else (item, None)
    out = f'<figure class="pfig">{asset(slug, ref)}'
    if cap:
        out += f"<figcaption>{esc(cap)}</figcaption>"
    return out + "</figure>"


def rows_html(slug, rows):
    out = []
    for row in rows:
        out.append(f'<div class="prow prow--{len(row)}">' + "".join(media(slug, i) for i in row) + "</div>")
    return "\n".join(out)


def facts_html(facts):
    return '<dl class="pfacts">' + "".join(
        f"<div><dt>{esc(k)}</dt><dd>{v}</dd></div>" for k, v in facts) + "</dl>"


NAV = '''      <nav class="navbar" aria-label="Main">
        <a class="navbar__item is-current" href="/" aria-current="page">Work</a>
        <a class="navbar__item" href="/about">About</a>
        <a class="navbar__item" href="/fun">Fun</a>
      </nav>'''


def page(p, nxt):
    s = p["slug"]
    nav_items = [("overview", "Overview")] + [(sec["id"], sec["nav"]) for sec in p["sections"] if sec.get("nav")]
    side_links = "\n".join(
        f'          <a class="chip" href="#{i}" data-section="{i}">{esc(n)}</a>' for i, n in nav_items)
    hero = media(s, p["hero"])
    overview = [f'<p class="phead__meta">{esc(p["meta"])}</p>',
                f'<h1 class="phead__title">{esc(p["title"])}</h1>',
                f'<p class="phead__summary">{esc(p["summary"])}</p>']
    if p.get("note"):
        overview.append(f'<p class="phead__note">{esc(p["note"])}</p>')
    deliver = ""
    if p.get("deliverables"):
        deliver = ('<div class="psec__deliver"><p class="psec__label">My deliverables</p><ol>' +
                   "".join(f"<li>{esc(d)}</li>" for d in p["deliverables"]) + "</ol></div>")
    secs = []
    for sec in p["sections"]:
        parts = [f'<section class="psec" id="{sec["id"]}">', f'<p class="psec__label">{esc(sec["label"])}</p>']
        if sec.get("heading"):
            parts.append(f'<h2 class="psec__heading">{esc(sec["heading"])}</h2>')
        if sec.get("body"):
            parts.append(f'<p class="psec__body">{esc(sec["body"])}</p>')
        if sec.get("flow"):
            parts.append('<ol class="pflow">' + "".join(f"<li>{esc(x)}</li>" for x in sec["flow"]) + "</ol>")
        if sec.get("facts"):
            parts.append(facts_html(sec["facts"]))
        if sec.get("link"):
            t, u = sec["link"]
            parts.append(f'<a class="pill pill--small psec__link" href="{esc(u)}" target="_blank" rel="noopener"><span>{esc(t)}</span></a>')
        if sec.get("rows"):
            parts.append(rows_html(s, sec["rows"]))
        parts.append("</section>")
        secs.append("\n".join(parts))
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#f7f7f7" />
  <title>{esc(p["card"])} — Jenna Choi</title>
  <meta name="description" content="{esc(p["summary"][:155])}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fustat:wght@400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/styles.css" />
</head>
<body class="project">
  <!-- Generated by tools/build_projects.py — edit the data there, then re-run. -->
  <div class="layout page-grid">
    <aside class="sidebar">
{NAV}

      <a class="back" href="/">← All work</a>

      <div class="control">
        <p class="control__label">On this page</p>
        <div class="filters">
{side_links}
        </div>
      </div>

      <div class="control sidebar__bottom">
        <p class="control__label">Next project</p>
        <a class="chip chip--next" href="/{nxt["slug"]}">{esc(nxt["card"])} →</a>
      </div>
    </aside>

    <main class="main pmain" aria-label="{esc(p["card"])}">
      <header class="phead" id="overview">
        {"".join(overview)}
      </header>
      <div class="prow prow--1 phero">{hero}</div>
      {facts_html(p["facts"])}
      {deliver}
{chr(10).join(secs)}

      <nav class="pnext">
        <a class="pill pill--small" href="/"><span>← Back to work</span></a>
        <a class="pnext__link" href="/{nxt["slug"]}"><span class="psec__label">Next project</span><span class="pnext__title">{esc(nxt["card"])} →</span></a>
      </nav>

      <footer class="site-footer">
        <p class="pill pill--small pill--center">© 2026 Jenna Choi</p>
        <a class="pill pill--small" href="#" data-link="email"><span>Email</span><span class="pill__arrow" aria-hidden="true">↗</span></a>
        <a class="pill pill--small" href="#" data-link="linkedin" target="_blank" rel="noopener"><span>LinkedIn</span><span class="pill__arrow" aria-hidden="true">↗</span></a>
        <a class="pill pill--small" href="#" data-link="resume" target="_blank" rel="noopener"><span>Resume</span><span class="pill__arrow" aria-hidden="true">↗</span></a>
      </footer>
    </main>
  </div>

  <script src="/main.js" defer></script>
</body>
</html>
'''


if __name__ == "__main__":
    for i, p in enumerate(PROJECTS):
        nxt = PROJECTS[(i + 1) % len(PROJECTS)]
        with open(os.path.join(ROOT, f'{p["slug"]}.html'), "w") as f:
            f.write(page(p, nxt))
        print("wrote", p["slug"] + ".html")
