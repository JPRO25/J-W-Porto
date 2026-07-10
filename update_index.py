import re

file_path = "index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update fonts
content = re.sub(
    r'<link href="https://fonts\.googleapis\.com/css2\?family=Lora.*?rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">',
    content
)

# 2. Remove cred-preview-box
content = re.sub(
    r'<!-- CREDENTIALS HOVER PREVIEW CONTAINER -->.*?<!-- PROJECT MODALS -->',
    '<!-- PROJECT MODALS -->',
    content,
    flags=re.DOTALL
)

# 3. Replace hero-sec
hero_old_pattern = r'<section class="hero-section" id="hero-sec">.*?</section>'
hero_new = '''<section class="hero-section" id="hero-sec">
            <div class="hero-container">
                <div class="hero-left">
                    <span class="hero-greeting">Hello, I'm</span>
                    <h1 class="hero-title">Julman Waruwu</h1>
                    <p class="hero-subtitle">IoT Developer & Smart Systems Engineer<br><span style="font-size: 0.85em; font-weight: 400; opacity: 0.8;">Computer Engineering Technology Student</span></p>
                    
                    <div class="hero-actions">
                        <a href="#contact-sec" class="btn-contact-me">Contact Me</a>
                    </div>
                    
                    <!-- Social Links -->
                    <div class="hero-social-links">
                        <a href="https://github.com/JPROGIPB" target="_blank" title="GitHub"><i class="fa-brands fa-github"></i></a>
                        <a href="https://linkedin.com/in/julwar-25-ai-eng" target="_blank" title="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
                        <a href="CV_ATS_Julman_Waruwu.pdf" target="_blank" title="Download Resume"><i class="fa-solid fa-file-arrow-down"></i></a>
                        <a href="mailto:julman.waruwu@gmail.com" title="Email"><i class="fa-regular fa-envelope"></i></a>
                        <a href="https://wa.me/6281234567890" target="_blank" title="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
                    </div>
                </div>
                
                <div class="hero-right hero-graphic-container">
                    <svg class="abstract-wave" viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <linearGradient id="waveGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#00e5ff" />
                                <stop offset="50%" stop-color="#3b82f6" />
                                <stop offset="100%" stop-color="#ff007f" />
                            </linearGradient>
                            <filter id="glow">
                                <feGaussianBlur stdDeviation="6" result="coloredBlur"/>
                                <feMerge>
                                    <feMergeNode in="coloredBlur"/>
                                    <feMergeNode in="SourceGraphic"/>
                                </feMerge>
                            </filter>
                        </defs>
                        <!-- A complex tech-looking wavy path -->
                        <path class="wave-path" d="M421.5,339.5Q386,429,285.5,444.5Q185,460,113,383Q41,306,75,207.5Q109,109,207.5,73Q306,37,381.5,108.5Q457,180,421.5,339.5Z" fill="none" stroke="url(#waveGradient)" stroke-width="6" filter="url(#glow)"/>
                        <path class="wave-path-2" d="M439.5,338.5Q379,427,276.5,431Q174,435,110.5,357Q47,279,77.5,177.5Q108,76,211.5,58.5Q315,41,407.5,110.5Q500,180,439.5,338.5Z" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="2"/>
                    </svg>
                    <!-- Floating Shapes -->
                    <div class="shape pill-magenta"></div>
                    <div class="shape circle-blue"></div>
                    <div class="shape badge-orange"></div>
                    <div class="shape square-cyan"></div>
                </div>
            </div>
        </section>'''

content = re.sub(hero_old_pattern, hero_new, content, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html updated successfully!")
