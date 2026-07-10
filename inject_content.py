from bs4 import BeautifulSoup
import re

with open("index_v1.html", "r", encoding="utf-8") as f:
    soup_old = BeautifulSoup(f, "html.parser")

with open("index.html", "r", encoding="utf-8") as f:
    html_new = f.read()

# 1. Extract Skills
skills_html = ""
skills_grid = soup_old.find("div", class_="skills-grid")
if skills_grid:
    for card in skills_grid.find_all("div", class_="skill-card"):
        icon = card.find("i")
        img = card.find("img")
        title = card.find("span", class_="skill-name")
        
        icon_html = ""
        if icon:
            icon_html = f'<i class="{icon.get("class")[0]} {icon.get("class")[1]}" style="font-size: 1.8rem; color: var(--accent-cyan);"></i>'
        elif img:
            img_src = img.get("src")
            icon_html = f'<img src="{img_src}" style="width: 30px; height: 30px; object-fit: contain;">'
            
        if title:
            skills_html += f'''
                    <div class="glass-card skill-card-v2" style="display: flex; align-items: center; gap: 1rem; padding: 1.5rem;">
                        {icon_html}
                        <div>
                            <h3 style="font-size: 1.1rem; font-weight: 500; margin: 0;">{title.text}</h3>
                        </div>
                    </div>'''

# 2. Extract Portfolio
portfolio_html = ""
port_grid = soup_old.find("div", class_="portfolio-grid")
if port_grid:
    for card in port_grid.find_all("div", class_="portfolio-card"):
        img_placeholder = card.find("div", class_="portfolio-image-placeholder")
        img_src = ""
        if img_placeholder and img_placeholder.find("img"):
            img_src = img_placeholder.find("img").get("src")
        
        info = card.find("div", class_="portfolio-card-info")
        meta = info.find("div", class_="card-meta") if info else None
        title = info.find("h3") if info else None
        desc = info.find("p") if info else None
        
        # We need an onclick action from the original card
        onclick = card.get("onclick", "")
        
        portfolio_html += f'''
                    <div class="glass-card port-card" {f'onclick="{onclick}" style="cursor: pointer;"' if onclick else ''}>
                        <div class="port-image" style="background-image: url('{img_src}');"></div>
                        <div class="port-content">
                            <span class="port-tag">{meta.text if meta else ''}</span>
                            <h3>{title.text if title else ''}</h3>
                            <p>{desc.text if desc else ''}</p>
                        </div>
                    </div>'''

# Inject Skills
html_new = re.sub(
    r'<div class="skills-grid"[^>]*>.*?</div>\s*</section>',
    f'<div class="skills-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 1rem;">\n{skills_html}\n                </div>\n            </section>',
    html_new,
    flags=re.DOTALL
)

# Inject Portfolio
html_new = re.sub(
    r'<div class="portfolio-grid">.*?</div>\s*</section>',
    f'<div class="portfolio-grid">\n{portfolio_html}\n                </div>\n            </section>',
    html_new,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_new)

print("Successfully injected Skills and Portfolio content to index.html!")
