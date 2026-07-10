import re
import os

html_file = r'C:\Users\Julman Waruwu\Documents\j&w-porto\index.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

grid_start = content.find('<div class="portfolio-grid">')
if grid_start == -1:
    print("Could not find portfolio-grid")
    exit()

grid_end_idx = content.find('</section>', grid_start)
if grid_end_idx == -1:
    print("Could not find end of portfolio section")
    exit()

# We need to backtrack to the exact closing div of the portfolio-grid.
# There is a <div class="portfolio-grid">...</div>, so the last </div> before </section>
last_div = content.rfind('</div>', grid_start, grid_end_idx)

cards_html = content[grid_start + len('<div class="portfolio-grid">'):last_div]

parts = cards_html.split('<!-- Project ')
if len(parts) > 1:
    cards = ['<!-- Project ' + p for p in parts[1:]]
else:
    print("Could not extract cards")
    exit()

featured_ids = ['bieon', 'sealen', 'presenthub', 'moocare']
featured_cards = []
other_cards = []

for card in cards:
    is_featured = False
    for fid in featured_ids:
        if f"openProjectModal('{fid}')" in card:
            card = card.replace('card-small', 'card-large')
            featured_cards.append((fid, card))
            is_featured = True
            break
    if not is_featured:
        card = card.replace('card-large', 'card-small')
        other_cards.append(card)

sorted_featured = []
for fid in featured_ids:
    for f_fid, f_card in featured_cards:
        if f_fid == fid:
            sorted_featured.append(f_card)
            break

new_grid_html = """<h3 class="subsection-title" style="margin-top: 20px; margin-bottom: 25px; font-size: 1.4rem; color: var(--text-color); border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px;">Featured Engineering Projects</h3>
            <div class="portfolio-grid" style="margin-bottom: 50px;">
""" + "".join(sorted_featured) + """            </div>

            <h3 class="subsection-title" style="margin-top: 40px; margin-bottom: 25px; font-size: 1.4rem; color: var(--text-color); border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px;">Other Projects & Explorations</h3>
            <div class="portfolio-grid">
""" + "".join(other_cards) + """            </div>"""

new_content = content[:grid_start] + new_grid_html + content[last_div + 6:]

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully split projects")
