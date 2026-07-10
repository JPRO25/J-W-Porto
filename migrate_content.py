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
        # convert to V2 style (glass-card style)
        icon = card.find("i")
        title = card.find("h3")
        desc = card.find("p")
        if icon and title:
            skills_html += f'''
                    <div class="glass-card skill-card-v2" style="display: flex; align-items: center; gap: 1rem; padding: 1.5rem;">
                        <i class="{icon.get('class')[0]} {icon.get('class')[1]}" style="font-size: 1.8rem; color: var(--accent-cyan);"></i>
                        <div>
                            <h3 style="font-size: 1.1rem; font-weight: 500;">{title.text}</h3>
                            <p style="font-size: 0.85rem; color: var(--text-secondary);">{desc.text if desc else ''}</p>
                        </div>
                    </div>'''

# 2. Extract Portfolio
portfolio_html = ""
port_grid = soup_old.find("div", class_="portfolio-grid")
if port_grid:
    for card in port_grid.find_all("div", class_="portfolio-card"):
        img_div = card.find("div", class_="card-image")
        img_style = img_div["style"] if img_div and img_div.has_attr("style") else ""
        meta = card.find("div", class_="card-meta")
        title = card.find("h3", class_="card-title")
        desc = card.find("p", class_="card-desc")
        
        portfolio_html += f'''
                    <div class="glass-card port-card">
                        <div class="port-image" style="{img_style}"></div>
                        <div class="port-content">
                            <span class="port-tag">{meta.text if meta else ''}</span>
                            <h3>{title.text if title else ''}</h3>
                            <p>{desc.text if desc else ''}</p>
                        </div>
                    </div>'''

# 3. Extract Certificates
certs_html = ""
cert_grid = soup_old.find("div", class_="credentials-list")
if cert_grid:
    for item in cert_grid.find_all("div", class_="cred-item"):
        year = item.find("div", class_="cred-year")
        title = item.find("h3", class_="cred-title")
        org = item.find("div", class_="cred-org")
        link = item.find("a", class_="cred-link")
        
        href = link['href'] if link else '#'
        
        certs_html += f'''
                    <a href="{href}" target="_blank" style="text-decoration: none; color: inherit;">
                        <div class="glass-card cert-card-v2" style="display: flex; justify-content: space-between; align-items: center; padding: 1.5rem; margin-bottom: 1rem;">
                            <div>
                                <h3 style="font-size: 1.1rem; font-weight: 500; margin-bottom: 0.2rem; color: var(--accent-cyan);">{title.text if title else ''}</h3>
                                <span style="font-size: 0.9rem; color: var(--text-secondary);">{org.text if org else ''}</span>
                            </div>
                            <div style="font-family: var(--font-secondary); font-weight: 700; color: rgba(255,255,255,0.2); font-size: 1.2rem;">
                                {year.text if year else ''}
                            </div>
                        </div>
                    </a>'''

# 4. Extract Experience
exp_html = ""
timeline = soup_old.find("div", class_="timeline")
if timeline:
    for item in timeline.find_all("div", class_="timeline-item"):
        date = item.find("div", class_="timeline-date")
        title = item.find("h3", class_="timeline-title")
        org = item.find("div", class_="timeline-org")
        desc = item.find("p", class_="timeline-desc")
        
        exp_html += f'''
                    <div class="glass-card exp-card-v2" style="position: relative; padding: 2rem; margin-bottom: 2rem; border-left: 4px solid var(--accent-magenta);">
                        <span style="display: inline-block; padding: 0.3rem 0.8rem; background: rgba(255,0,127,0.1); color: var(--accent-magenta); border-radius: 20px; font-size: 0.8rem; font-weight: 600; margin-bottom: 1rem;">{date.text if date else ''}</span>
                        <h3 style="font-size: 1.3rem; margin-bottom: 0.2rem;">{title.text if title else ''}</h3>
                        <div style="font-family: var(--font-secondary); font-size: 0.9rem; color: var(--accent-orange); margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 1px;">{org.text if org else ''}</div>
                        <p style="color: var(--text-secondary); font-size: 0.95rem;">{desc.text if desc else ''}</p>
                    </div>'''


# Now, assemble the full right pane content
new_right_content = f'''
            <!-- 1. Hero Text Section (First Viewport) -->
            <section class="hero-text-section" id="hero">
                <div class="hero-label">
                    Julman Waruwu<br>
                    <strong>Portfolio Archive</strong>
                </div>
                <h1 class="hero-title">Build Your Future<br>With Intelligent<br>Systems</h1>
                <p class="hero-subtitle">
                    Pursue real-world solutions through automation, IoT, and edge AI integration designed for efficiency and backed by engineering expertise.
                </p>
                <div class="hero-actions">
                    <a href="#portfolio" class="btn-primary">View Portfolio</a>
                    <a href="CV_ATS_Julman_Waruwu.pdf" target="_blank" class="btn-secondary">Download CV</a>
                </div>
            </section>

            <!-- 2. About Section -->
            <section id="about" class="content-section">
                <h2 class="section-title">About Me</h2>
                <div class="glass-card">
                    <p>I am dedicated to designing and building smart automation systems (<strong>IoT</strong>) and <strong>Embedded Systems</strong>. Backed by skills in <strong>Web Applications (React/Node.js)</strong>, <strong>Python Development</strong>, <strong>Edge AI (TinyML)</strong> on microcontrollers, and <strong>3D CAD (Fusion 360)</strong>, I can bring product ideas to life from conceptual sketches to fully production-ready prototypes.</p>
                </div>
            </section>
            
            <!-- 3. Experience Section -->
            <section id="experience" class="content-section">
                <h2 class="section-title">Experience</h2>
                <div class="experience-list">
{exp_html}
                </div>
            </section>

            <!-- 4. Skills Section -->
            <section id="skills" class="content-section">
                <h2 class="section-title">Technical Capabilities</h2>
                <div class="skills-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 1rem;">
{skills_html}
                </div>
            </section>

            <!-- 5. Portfolio Section -->
            <section id="portfolio" class="content-section">
                <h2 class="section-title">Featured Works</h2>
                <div class="portfolio-grid">
{portfolio_html}
                </div>
            </section>
            
            <!-- 6. Certificates Section -->
            <section id="certificates" class="content-section">
                <h2 class="section-title">Certifications</h2>
                <div class="certificates-list">
{certs_html}
                </div>
            </section>

            <!-- 7. Contact Section -->
            <section id="contact" class="content-section">
                <h2 class="section-title">Get In Touch</h2>
                <div class="glass-card" style="text-align: center;">
                    <p style="margin-bottom: 2rem; color: var(--text-secondary);">Interested in collaborating or have a project in mind? Let's talk.</p>
                    <a href="mailto:julman.waruwu@gmail.com" class="btn-primary" style="margin: 0; background: var(--accent-cyan); color: #000; border: none; font-weight: 600;">Email Me</a>
                    <div style="margin-top: 2rem; display: flex; justify-content: center; gap: 1.5rem; font-size: 1.5rem;">
                        <a href="https://github.com/JPROGIPB" target="_blank" style="color: var(--text-primary);"><i class="fa-brands fa-github"></i></a>
                        <a href="https://linkedin.com/in/julwar-25-ai-eng" target="_blank" style="color: var(--text-primary);"><i class="fa-brands fa-linkedin-in"></i></a>
                    </div>
                </div>
            </section>
            
            <!-- Footer spacing -->
            <div style="height: 100px;"></div>
'''

# Replace the split-right content in index.html
html_new = re.sub(
    r'<div class="split-right">.*?<!-- Footer spacing -->\s*<div style="height: 100px;"></div>\s*</div>',
    f'<div class="split-right">\n{new_right_content}\n        </div>',
    html_new,
    flags=re.DOTALL
)

# Also add a minimalist navigation sidebar (vertical dots on the right edge)
nav_html = '''
    <!-- Sticky Navigation Dots -->
    <nav style="position: fixed; right: 2rem; top: 50%; transform: translateY(-50%); display: flex; flex-direction: column; gap: 1rem; z-index: 100;">
        <a href="#hero" title="Home" style="width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,0.3); transition: 0.3s;"></a>
        <a href="#about" title="About" style="width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,0.3); transition: 0.3s;"></a>
        <a href="#experience" title="Experience" style="width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,0.3); transition: 0.3s;"></a>
        <a href="#skills" title="Skills" style="width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,0.3); transition: 0.3s;"></a>
        <a href="#portfolio" title="Portfolio" style="width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,0.3); transition: 0.3s;"></a>
        <a href="#certificates" title="Certificates" style="width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,0.3); transition: 0.3s;"></a>
    </nav>
'''
html_new = html_new.replace('<!-- LEFT: FIXED GRAPHIC -->', nav_html + '\n        <!-- LEFT: FIXED GRAPHIC -->')


with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_new)

print("Successfully migrated all content to index.html!")
