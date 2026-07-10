import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Julman Waruwu | Smart Systems Engineer</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style_v2.css">
</head>
<body>

    <!-- Split Layout Wrapper -->
    <main class="split-layout">
        
        <!-- LEFT: FIXED GRAPHIC -->
        <div class="split-left">
            <div class="graphic-container">
                <!-- SVG Wave mimicking Cisco outline -->
                <svg class="abstract-wave" viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">
                    <defs>
                        <linearGradient id="waveGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                            <stop offset="0%" stop-color="#0066ff" />   <!-- Blue -->
                            <stop offset="25%" stop-color="#00ccff" />  <!-- Cyan -->
                            <stop offset="75%" stop-color="#ff007f" />  <!-- Magenta -->
                            <stop offset="100%" stop-color="#ff6600" /> <!-- Orange -->
                        </linearGradient>
                    </defs>
                    <!-- Bloby wavy star shape on the left edge (partially cut off) -->
                    <path class="wave-path" d="M120,50 Q180,20 220,60 T300,100 T330,180 T290,260 T320,340 T270,410 T180,430 T120,490 T50,450 T-20,400 T-40,250 T20,100 Z" fill="none" stroke="url(#waveGradient)" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                
                <!-- Floating Elements (Exactly like the Cisco image) -->
                <div class="shape pill-magenta"></div>
                <div class="shape circle-blue"></div>
                <div class="shape star-orange"></div>
                <div class="shape square-cyan"></div>
            </div>
        </div>

        <!-- RIGHT: SCROLLABLE CONTENT -->
        <div class="split-right">
            
            <!-- 1. Hero Text Section (First Viewport) -->
            <section class="hero-text-section">
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

            <!-- 3. Portfolio Section -->
            <section id="portfolio" class="content-section">
                <h2 class="section-title">Featured Works</h2>
                <div class="portfolio-grid">
                    <div class="glass-card port-card">
                        <div class="port-image" style="background-image: url('assets/images/bieon_ecosense.jpg');"></div>
                        <div class="port-content">
                            <span class="port-tag">IoT // Ecosystem</span>
                            <h3>Bieon Ecosense</h3>
                            <p>Ekosistem smart home living terintegrasi hemat daya.</p>
                        </div>
                    </div>
                    <div class="glass-card port-card">
                        <div class="port-image" style="background-image: url('assets/images/siro.jpg');"></div>
                        <div class="port-content">
                            <span class="port-tag">IoT // Agriculture</span>
                            <h3>Siro - Irigasi Otomatis</h3>
                            <p>Sistem irigasi otomatis cerdas berbasis IoT.</p>
                        </div>
                    </div>
                </div>
            </section>
            
            <!-- Footer spacing -->
            <div style="height: 100px;"></div>
        </div>

    </main>

</body>
</html>"""

css_content = """/* ==========================================================================
   RESET & BASE VARIABLES
   ========================================================================== */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --bg-color: #0b1120; /* Deep navy exactly like Cisco */
    --text-primary: #ffffff;
    --text-secondary: #94a3b8;
    
    --font-primary: 'Inter', sans-serif;
    --font-secondary: 'Roboto', sans-serif;
    
    --accent-cyan: #00ccff;
    --accent-magenta: #ff007f;
    --accent-orange: #ff6600;
}

body {
    background-color: var(--bg-color);
    color: var(--text-primary);
    font-family: var(--font-primary);
    line-height: 1.6;
    overflow-x: hidden;
}

/* ==========================================================================
   SPLIT LAYOUT
   ========================================================================== */
.split-layout {
    display: flex;
    width: 100%;
    min-height: 100vh;
}

/* LEFT PANE - FIXED GRAPHIC */
.split-left {
    position: fixed;
    top: 0;
    left: 0;
    width: 50vw;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: flex-start; /* Align graphic to the left edge */
    z-index: 10;
    pointer-events: none; /* Let clicks pass through if needed */
}

/* RIGHT PANE - SCROLLABLE CONTENT */
.split-right {
    margin-left: 50vw;
    width: 50vw;
    min-height: 100vh;
    padding: 0;
    z-index: 1;
}

/* ==========================================================================
   GRAPHIC ELEMENTS (CISCO STYLE)
   ========================================================================== */
.graphic-container {
    position: relative;
    width: 100%;
    height: 100%;
    max-width: 600px;
}

.abstract-wave {
    position: absolute;
    top: 50%;
    left: -100px; /* Shift to the left edge to crop it like the image */
    transform: translateY(-50%);
    width: 600px;
    height: 600px;
    animation: slowPulse 10s infinite alternate;
}

@keyframes slowPulse {
    0% { transform: translateY(-50%) scale(1) rotate(0deg); }
    100% { transform: translateY(-50%) scale(1.05) rotate(5deg); }
}

/* Floating Shapes */
.shape {
    position: absolute;
    box-shadow: 0 4px 20px rgba(0,0,0,0.5);
}

.pill-magenta {
    width: 40px;
    height: 50px;
    background-color: #ff007f;
    border-radius: 40px 0 0 40px; /* Half pill like image */
    top: 20%;
    left: 300px;
    animation: float1 5s ease-in-out infinite;
}

.circle-blue {
    width: 25px;
    height: 25px;
    background-color: #0066ff;
    border-radius: 50%;
    top: 25%;
    left: 250px;
    animation: float2 7s ease-in-out infinite alternate;
}

.star-orange {
    width: 50px;
    height: 50px;
    background-color: #ff8c00;
    /* 8-pointed smooth star shape */
    clip-path: polygon(30% 0%, 70% 0%, 100% 30%, 100% 70%, 70% 100%, 30% 100%, 0% 70%, 0% 30%);
    bottom: 20%;
    left: 100px;
    animation: float3 6s ease-in-out infinite;
}

.square-cyan {
    width: 25px;
    height: 25px;
    background-color: #00e5ff;
    border-radius: 6px 0 6px 0; /* weird skewed squircle */
    transform: skew(-15deg, -15deg);
    bottom: 25%;
    left: 200px;
    animation: float4 8s ease-in-out infinite;
}

@keyframes float1 { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-15px); } }
@keyframes float2 { 0%, 100% { transform: translateY(0) scale(1); } 50% { transform: translateY(10px) scale(1.1); } }
@keyframes float3 { 0%, 100% { transform: translateY(0) rotate(0deg); } 50% { transform: translateY(-10px) rotate(15deg); } }
@keyframes float4 { 0%, 100% { transform: translateY(0) rotate(0deg); } 50% { transform: translateY(-20px) rotate(-10deg); } }

/* ==========================================================================
   HERO TEXT SECTION
   ========================================================================== */
.hero-text-section {
    min-height: 100vh; /* Take full height of right pane initially */
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 2rem 4rem 2rem 2rem;
}

.hero-label {
    font-family: var(--font-secondary);
    font-size: 0.85rem;
    color: var(--text-primary);
    margin-bottom: 2rem;
    line-height: 1.4;
    letter-spacing: 0.5px;
}
.hero-label strong {
    font-weight: 700;
}

.hero-title {
    font-family: var(--font-primary);
    font-size: 4rem;
    font-weight: 200; /* Ultra Light */
    line-height: 1.1;
    margin-bottom: 1.5rem;
    letter-spacing: -1.5px;
}

.hero-subtitle {
    font-family: var(--font-secondary);
    font-size: 1.1rem;
    font-weight: 400;
    color: #cbd5e1;
    max-width: 500px;
    line-height: 1.6;
    margin-bottom: 3rem;
}

/* ==========================================================================
   CONTENT SECTIONS & COMPONENTS
   ========================================================================== */
.content-section {
    padding: 4rem 4rem 2rem 2rem;
}

.section-title {
    font-size: 2rem;
    font-weight: 300;
    margin-bottom: 2rem;
    letter-spacing: -0.5px;
}

.glass-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    padding: 2rem;
    transition: all 0.3s ease;
}

.glass-card:hover {
    background: rgba(255, 255, 255, 0.06);
    border-color: rgba(255, 255, 255, 0.1);
}

.portfolio-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
}

.port-card {
    padding: 0;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}

.port-image {
    width: 100%;
    height: 250px;
    background-size: cover;
    background-position: center;
}

.port-content {
    padding: 1.5rem;
}

.port-tag {
    font-family: var(--font-secondary);
    font-size: 0.75rem;
    color: var(--accent-orange);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 0.5rem;
    display: block;
}

.port-content h3 {
    font-weight: 400;
    font-size: 1.3rem;
    margin-bottom: 0.5rem;
}

.port-content p {
    color: var(--text-secondary);
    font-size: 0.95rem;
}

/* Buttons */
.btn-primary {
    display: inline-block;
    padding: 0.8rem 2rem;
    background: transparent;
    color: var(--text-primary);
    text-decoration: none;
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 30px;
    font-size: 0.9rem;
    transition: all 0.3s ease;
    margin-right: 1rem;
}
.btn-primary:hover {
    background: rgba(255,255,255,0.1);
}
.btn-secondary {
    display: inline-block;
    padding: 0.8rem 2rem;
    background: transparent;
    color: var(--accent-cyan);
    text-decoration: none;
    font-size: 0.9rem;
    transition: all 0.3s ease;
}
.btn-secondary:hover {
    color: #fff;
}

/* ==========================================================================
   MOBILE RESPONSIVENESS
   ========================================================================== */
@media (max-width: 950px) {
    .split-layout {
        flex-direction: column;
    }
    .split-left {
        position: relative;
        width: 100%;
        height: 60vh;
        min-height: auto;
        justify-content: center;
        overflow: hidden;
    }
    .abstract-wave {
        left: 50%;
        transform: translate(-50%, -50%);
    }
    .shape {
        transform: scale(0.7); /* make particles smaller */
    }
    .split-right {
        margin-left: 0;
        width: 100%;
    }
    .hero-text-section {
        min-height: auto;
        padding: 4rem 2rem;
    }
    .hero-title {
        font-size: 3rem;
    }
    .content-section {
        padding: 2rem;
    }
}
"""

with open("index_v2.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("style_v2.css", "w", encoding="utf-8") as f:
    f.write(css_content)

print("Generated index_v2.html and style_v2.css")
