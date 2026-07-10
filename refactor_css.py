import re

file_path = "style.css"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Append split layout CSS
split_css = '''
/* ==========================================================================
   SPLIT SCREEN LAYOUT
   ========================================================================== */
.split-layout-wrapper {
    display: flex;
    width: 100%;
    min-height: 100vh;
    background-color: var(--bg-primary);
}

.split-left {
    position: fixed;
    top: 0;
    left: 0;
    width: 50%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 4rem;
    z-index: 10;
    overflow: hidden;
}

.split-right {
    margin-left: 50%;
    width: 50%;
    min-height: 100vh;
    padding: 0;
    z-index: 1;
}

/* Redesign Hero within Split Left */
.hero-section {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    padding: 0;
    background: transparent !important;
}

.hero-container {
    flex-direction: column-reverse; /* Text below graphic */
    gap: 2rem;
    width: 100%;
    max-width: 100%;
}

.hero-left {
    width: 100%;
}

.hero-right {
    width: 100%;
    justify-content: flex-start;
    margin-bottom: 2rem;
}

.hero-graphic-container {
    width: 300px;
    height: 300px;
}

.hero-section::before, .hero-section::after {
    display: none; /* We'll move the glow to split-left */
}

.split-left::before {
    content: '';
    position: absolute;
    bottom: -10%;
    left: -10%;
    width: 70%;
    height: 70%;
    background: radial-gradient(circle, rgba(0, 229, 255, 0.15) 0%, transparent 70%);
    filter: blur(80px);
    z-index: 0;
}
.split-left::after {
    content: '';
    position: absolute;
    top: -10%;
    right: -10%;
    width: 70%;
    height: 70%;
    background: radial-gradient(circle, rgba(255, 0, 127, 0.15) 0%, transparent 70%);
    filter: blur(80px);
    z-index: 0;
}

/* Sections inside split-right */
.split-right section {
    max-width: 800px;
    margin: 0 auto;
    padding: 6rem 3rem 4rem 3rem;
}

@media (max-width: 950px) {
    .split-layout-wrapper {
        flex-direction: column;
    }
    .split-left {
        position: relative;
        width: 100%;
        height: auto;
        min-height: 100vh;
        padding: 6rem 2rem;
    }
    .split-right {
        margin-left: 0;
        width: 100%;
    }
}
'''

# Remove any existing background-color from sections
content = re.sub(r'background-color:\s*#[a-fA-F0-9]{3,6};', '', content)
content = re.sub(r'background:\s*#121212;', '', content)
# Ensure section background is transparent
content = re.sub(r'section\s*\{', 'section {\n    background-color: transparent !important;', content)

# Remove old hero-section background gradients explicitly if they exist
content = re.sub(r'background:\s*linear-gradient.*?#121212.*?\);', '', content)

content += split_css

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("style.css split layout updated!")
