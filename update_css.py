import re

file_path = "style.css"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace body styles
content = re.sub(
    r'body \{\s*background-color: var\(--bg-primary\);\s*color: var\(--text-primary\);',
    'body {\n    background-color: var(--bg-primary);\n    color: var(--text-primary);\n    background-image: radial-gradient(circle at top left, rgba(0,229,255,0.05) 0%, transparent 40%),\n                      radial-gradient(circle at bottom right, rgba(255,0,127,0.05) 0%, transparent 40%);',
    content
)

# Replace Hero CSS block (from .hero-section to .profile-avatar-img)
hero_css_old_pattern = r'/\* Hero Section.*?\.profile-avatar-img \{.*?\n\}'
hero_css_new = '''/* Hero Section (Tech Dark Mode) */
.hero-section {
    position: relative;
    background-color: transparent;
    width: 100%;
    padding: 12rem 2.5rem 8rem 2.5rem;
    display: flex;
    align-items: center;
    overflow: hidden;
}

/* Ambient glow in hero */
.hero-section::before {
    content: '';
    position: absolute;
    bottom: -10%;
    left: -10%;
    width: 50%;
    height: 50%;
    background: radial-gradient(circle, rgba(0, 229, 255, 0.15) 0%, transparent 70%);
    filter: blur(80px);
    z-index: 0;
}
.hero-section::after {
    content: '';
    position: absolute;
    top: -10%;
    right: -10%;
    width: 50%;
    height: 50%;
    background: radial-gradient(circle, rgba(255, 0, 127, 0.15) 0%, transparent 70%);
    filter: blur(80px);
    z-index: 0;
}

.hero-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    gap: 4rem;
    position: relative;
    z-index: 2;
}

.hero-left {
    flex: 1;
    z-index: 3;
}

.hero-right {
    flex: 1;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    position: relative;
}

/* Hero Graphic Container & Animations */
.hero-graphic-container {
    position: relative;
    width: 500px;
    height: 500px;
    perspective: 1000px;
}

.abstract-wave {
    width: 100%;
    height: 100%;
    animation: rotateSlow 25s linear infinite;
}

.wave-path {
    animation: morphWave 8s ease-in-out infinite alternate;
}

.wave-path-2 {
    animation: rotateSlow 15s linear infinite reverse;
    transform-origin: center;
}

/* Floating Geometric Shapes */
.shape {
    position: absolute;
    backdrop-filter: blur(5px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

.pill-magenta {
    width: 60px;
    height: 30px;
    background: linear-gradient(135deg, #ff007f, #ff4d4d);
    border-radius: 30px;
    top: 15%;
    right: 25%;
    animation: floatShape1 6s ease-in-out infinite;
}

.circle-blue {
    width: 25px;
    height: 25px;
    background: #3b82f6;
    border-radius: 50%;
    top: 25%;
    right: 65%;
    animation: floatShape2 8s ease-in-out infinite;
}

.badge-orange {
    width: 45px;
    height: 45px;
    background: #ff8c00;
    clip-path: polygon(50% 0%, 90% 20%, 100% 60%, 75% 100%, 25% 100%, 0% 60%, 10% 20%);
    bottom: 20%;
    left: 10%;
    animation: floatShape3 7s ease-in-out infinite;
}

.square-cyan {
    width: 25px;
    height: 25px;
    background: #00e5ff;
    border-radius: 4px;
    transform: rotate(15deg);
    bottom: 30%;
    left: 30%;
    animation: floatShape4 9s ease-in-out infinite;
}

@keyframes rotateSlow {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

@keyframes morphWave {
    0% { d: path("M421.5,339.5Q386,429,285.5,444.5Q185,460,113,383Q41,306,75,207.5Q109,109,207.5,73Q306,37,381.5,108.5Q457,180,421.5,339.5Z"); }
    50% { d: path("M439.5,338.5Q379,427,276.5,431Q174,435,110.5,357Q47,279,77.5,177.5Q108,76,211.5,58.5Q315,41,407.5,110.5Q500,180,439.5,338.5Z"); }
    100% { d: path("M421.5,339.5Q386,429,285.5,444.5Q185,460,113,383Q41,306,75,207.5Q109,109,207.5,73Q306,37,381.5,108.5Q457,180,421.5,339.5Z"); }
}

@keyframes floatShape1 {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(10deg); }
}
@keyframes floatShape2 {
    0%, 100% { transform: translateY(0) scale(1); }
    50% { transform: translateY(20px) scale(1.2); }
}
@keyframes floatShape3 {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-15px) rotate(-15deg); }
}
@keyframes floatShape4 {
    0%, 100% { transform: translateY(0) rotate(15deg); }
    50% { transform: translateY(-25px) rotate(45deg); }
}'''

# Replace from /* Hero Section to .profile-avatar-img
# It's tricky to regex multiline across 100+ lines. Let's just find the start and end string index.
start_idx = content.find("/* Hero Section")
end_idx = content.find("/* Section Headings */")

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + hero_css_new + "\n\n" + content[end_idx:]

# Let's write the modified content back
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("style.css hero section updated successfully!")
