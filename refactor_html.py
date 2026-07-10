import re

file_path = "index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Make hero-left content exactly like Cisco image
hero_left_new = '''<div class="hero-left">
                    <div style="margin-bottom: 2rem;">
                        <span style="font-family: var(--font-primary); font-size: 0.9rem; color: #ffffff; font-weight: 600;">J.W</span><br>
                        <span style="font-family: var(--font-primary); font-size: 0.8rem; color: var(--text-secondary); font-weight: 500;">Portofolio<br>Archive</span>
                    </div>
                    <h1 class="hero-title" style="font-family: var(--font-primary); font-size: 3.5rem; font-weight: 300; letter-spacing: -1px; margin-top: 1rem; margin-bottom: 1rem; line-height: 1.15; color: #ffffff;">Julman<br>Waruwu</h1>
                    <p class="hero-subtitle" style="font-family: var(--font-primary); font-size: 1.05rem; color: var(--text-secondary); font-weight: 300; max-width: 400px; line-height: 1.6; margin-bottom: 2.5rem;">
                        Pursue real career paths through intelligent automation and edge AI systems built for the future.
                    </p>
                    
                    <div class="hero-actions" style="display: flex; gap: 1rem; align-items: center; margin-bottom: 2.5rem;">
                        <a href="#contact-sec" class="btn-contact-me" style="background: transparent; color: #ffffff; border: 1px solid rgba(255,255,255,0.3); padding: 0.7rem 2rem; border-radius: 30px; font-weight: 400; transition: all 0.3s;">Contact Me</a>
                    </div>
                </div>'''

content = re.sub(
    r'<div class="hero-left">.*?</div>\s*<div class="hero-right hero-graphic-container">',
    hero_left_new + '\n                <div class="hero-right hero-graphic-container">',
    content,
    flags=re.DOTALL
)

# Apply split layout wrappers
content = content.replace('<main class="main-wrapper">', '<main class="main-wrapper split-layout-wrapper">\n        <div class="split-left">')
content = content.replace('</section>\n\n        <!-- 01. About Section -->', '</section>\n        </div>\n\n        <div class="split-right">\n        <!-- 01. About Section -->')
content = content.replace('    </main>', '        </div>\n    </main>')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html split layout structure updated!")
