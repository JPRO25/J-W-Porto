// ==========================================================================
// PROJECT DATA & MODALS (INSTAGRAM REELS INTEGRATED)
// ==========================================================================
const projectData = {
    bieon: {
        title: "Bieon Ecosense: Ecosystem Smart Home Living",
        tag: "IOT // ECOSYSTEM",
        videoFormat: "landscape",
        body: `
            <p><strong>Bieon Ecosense</strong> is a highly integrated smart home ecosystem focusing on low energy, low cost, and high flexibility.</p>
            
            <h4>Impact & Technical Highlights:</h4>
            <ul>
                <li><strong>Energy Efficiency:</strong> Reduced daily smart home energy consumption by 30% through optimized sleep protocols on ESP32 nodes.</li>
                <li><strong>Universal Compatibility:</strong> Engineered a central gateway capable of bridging proprietary custom nodes with major commercial smart devices.</li>
            </ul>
            <a href="https://github.com/JPROGIPB" target="_blank" class="btn-primary" style="margin-top: 15px; display: inline-block;">View Repository <i class="fa-solid fa-arrow-right"></i></a>
        `
    },
    siro: {
        title: "Siro - Irigasi Otomatis",
        tag: "IOT // IRRIGATION",
        videoFormat: "landscape",
        body: `
            <p><strong>Siro</strong> adalah sebuah proyek inovatif sistem irigasi otomatis berbasis IC Gal yang dirancang khusus untuk meningkatkan efisiensi penggunaan air pada sektor pertanian.</p>
            
            <h4>Fitur & Spesifikasi:</h4>
            <ul>
                <li><strong>Kontrol Otomatis:</strong> Menggunakan IC logika terprogram untuk memantau kelembaban tanah secara periodik dan menyiram tanaman secara presisi.</li>
                <li><strong>Efisiensi Tinggi:</strong> Mengurangi pemborosan air dan memastikan tanaman mendapatkan asupan air yang optimal sesuai kebutuhan aktual.</li>
            </ul>
        `
    },
    lactos: {
        title: "Lactos - Laci Otomatis",
        tag: "IOT // HOME UTILITY",
        videoFormat: "portrait",
        reelId: "DKvsPB3SMic",
        body: `
            <p><strong>Lactos</strong> adalah proyek laci otomatis pintar dengan sistem kendali terintegrasi langsung pada unit laci untuk kebutuhan rumah tangga modern.</p>
            
            <h4>Fitur & Spesifikasi:</h4>
            <ul>
                <li><strong>Control Panel Terintegrasi:</strong> Kendali buka/tutup laci dilakukan melalui panel kontrol fisik yang terpasang langsung di bagian depan laci.</li>
                <li><strong>Sistem Elektromekanik:</strong> Integrasi micro-controller, motor DC penggerak, limit switch, dan rel mekanis untuk pergerakan laci yang halus dan aman.</li>
            </ul>
        `
    },
    sealen: {
        title: "Sealen - Ocean Cleaner Robot",
        tag: "ROBOTICS // AI // ML",
        videoFormat: "landscape",
        body: `
            <p><strong>Sealen</strong> is a multidisciplinary collaborative project combining Edge AI and robotics to autonomously navigate and clean ocean debris.</p>
            
            <h4>Impact & Technical Highlights:</h4>
            <ul>
                <li><strong>Autonomous Navigation:</strong> Achieved a 95% obstacle avoidance rate using Reinforcement Learning on custom maritime simulation.</li>
                <li><strong>Efficient Routing:</strong> Reduced patrol distance by 40% utilizing optimized coordinate mapping algorithms.</li>
            </ul>
            <a href="https://github.com/JPROGIPB/SEALEN" target="_blank" class="btn-primary" style="margin-top: 15px; display: inline-block;">View Repository <i class="fa-solid fa-arrow-right"></i></a>
        `
    },
    chopx: {
        title: "Chop-X - Chicken Feed Cutter",
        tag: "IOT // INDUSTRIAL CONTROL",
        videoFormat: "landscape",
        body: `
            <p><strong>Chop-X</strong> adalah sistem pencacah pakan ayam berbasis embedded system yang dirancang untuk kebutuhan efisiensi operasional peternakan komersial.</p>
            
            <h4>Fitur & Spesifikasi:</h4>
            <ul>
                <li><strong>Kontrol Elektronik Variabel:</strong> Pengaturan kecepatan potong (variable speed) dan opsi mode pemotongan (cutter mode) melalui sirkuit kontrol elektronik.</li>
                <li><strong>Web Business Cost Calculator:</strong> Terintegrasi dengan dashboard berbasis web untuk menghitung konsumsi daya listrik dan biaya operasional bisnis secara akurat.</li>
            </ul>
        `
    },
    presenthub: {
        title: "Present Hub - Face Recognition Attendance",
        tag: "AI // FACE RECOGNITION",
        videoFormat: "landscape",
        body: `
            <p><strong>Present Hub</strong> is a student attendance system utilizing face recognition to drastically accelerate classroom check-ins.</p>
            
            <h4>Impact & Technical Highlights:</h4>
            <ul>
                <li><strong>Time Efficiency:</strong> Reduced classroom attendance processing time from 15 minutes to less than 3 minutes per session.</li>
                <li><strong>Anti-Spoofing:</strong> Integrated liveness detection to prevent spoofing via photos or smartphone screens with 98% accuracy.</li>
            </ul>
            <a href="https://github.com/JPROGIPB/PresentHub-AI-Attendance-System" target="_blank" class="btn-primary" style="margin-top: 15px; display: inline-block;">View Repository <i class="fa-solid fa-arrow-right"></i></a>
        `
    },
    yourpath: {
        title: "Your Path - AI CV Analyzer",
        tag: "AI // DATA SCIENCE // COLLAB",
        videoFormat: "landscape",
        body: `
            <p><strong>Your Path</strong> adalah proyek kolaborasi antar learning path pada program Dicoding Camp by DBS Foundation 2026, menggabungkan keahlian AI Engineer, Data Science, dan Fullstack Web Developer.</p>
            
            <h4>Fitur & Spesifikasi:</h4>
            <ul>
                <li><strong>Model Random Forest:</strong> Mengklasifikasikan hasil analisis CV berdasarkan data kecocokan kriteria (data pontik) untuk peran Data Science dan AI.</li>
                <li><strong>Integrasi Model LLM:</strong> Memanfaatkan model bahasa besar (LLM) untuk merangkum hasil klasifikasi dan menyusun saran serta rekomendasi pengembangan skill yang presisi bagi pengguna.</li>
            </ul>
        `
    },
    nodezero: {
        title: "Node Zero - Cybersecurity Testing",
        tag: "CYBERSECURITY // PENETRATION",
        videoFormat: "landscape",
        body: `
            <p><strong>Node Zero Project</strong> adalah proyek audit keamanan siber menggunakan distribusi sistem operasi khusus NodeZero untuk menganalisis celah keamanan situs web.</p>
            
            <h4>Fitur & Spesifikasi:</h4>
            <ul>
                <li><strong>Port Scanning & Analysis:</strong> Mendeteksi port terbuka dan menganalisis paket data yang lewat menggunakan kombinasi Wireshark dan Nmap.</li>
                <li><strong>Metasploit Exploitation:</strong> Melakukan simulasi penetration testing terkendali untuk menguji kerentanan sistem terhadap eksploitasi keamanan eksternal.</li>
            </ul>
        `
    },
    k1wireless: {
        title: "K1 Wireless - Enterprise IoT Network",
        tag: "NETWORK // ROUTEROS",
        videoFormat: "landscape",
        body: `
            <p><strong>K1 Wireless</strong> adalah proyek rancang bangun jaringan terpusat berskala enterprise secara virtual yang didedikasikan untuk kebutuhan pertukaran data sistem IoT.</p>
            
            <h4>Fitur & Spesifikasi:</h4>
            <ul>
                <li><strong>RouterOS Integration:</strong> Kombinasi router fisik dan router virtual (RouterOS) yang dikonfigurasi sebagai access point, router utama, dan web server lokal.</li>
                <li><strong>Virtual Sandbox Client:</strong> Menjalankan client virtual berbasis Ubuntu di dalam Virtual Machine (VM) untuk menguji kestabilan jaringan, bandwidth routing, dan latensi transmisi sensor.</li>
            </ul>
        `
    },
    ligatek: {
        title: "LigateK Board - Sports Scoreboard",
        tag: "EMBEDDED // SPORTS",
        videoFormat: "landscape",
        body: `
            <p><strong>LigateK Board</strong> adalah papan skor digital kustom yang dirancang khusus untuk mendukung kegiatan kompetisi olahraga tahunan Ligatek tingkat prodi.</p>
            
            <h4>Fitur & Spesifikasi:</h4>
            <ul>
                <li><strong>Sirkuit Digital Dasar:</strong> Dibangun murni memanfaatkan kombinasi IC logika dasar, dekoder 7-segment, gerbang logika, dan pencacah pulsa (counter IC).</li>
                <li><strong>Operasional Handal:</strong> Minim kegagalan sistem karena tidak menggunakan mikrokontroler kompleks, sehingga sangat andal untuk penggunaan luar ruangan.</li>
            </ul>
        `
    },
    parking: {
        title: "Mall Area Parking Automation",
        tag: "AUTOMATION // SIMULATION",
        videoFormat: "landscape",
        body: `
            <p><strong>Mall Area Parking Automation</strong> adalah proyek rancang bangun dan simulasi sistem parkir otomatis terintegrasi untuk pusat perbelanjaan.</p>
            
            <h4>Fitur & Spesifikasi:</h4>
            <ul>
                <li><strong>Overload Prevention:</strong> Sistem secara otomatis menghitung sisa slot parkir dan menutup palang pintu masuk utama jika kapasitas parkir terdeteksi penuh.</li>
                <li><strong>Peningkatan Keamanan:</strong> Integrasi kartu RF/sensor proximity pada gerbang masuk untuk pencatatan plat kendaraan dan peningkatan keamanan area parkir.</li>
            </ul>
        `
    },
    tekwan: {
        title: "TekWan 04 - L2VPN VPLS",
        tag: "NETWORK // L2VPN MPLS",
        videoFormat: "landscape",
        body: `
            <p><strong>TekWan 04 Project</strong> adalah proyek perancangan jaringan virtual untuk mengimplementasikan interkoneksi situs-situs customer menggunakan teknologi L2VPN MPLS (VPLS).</p>
            
            <h4>Fitur & Spesifikasi:</h4>
            <ul>
                <li><strong>Emulasi VPLS:</strong> Menghubungkan beberapa jaringan LAN customer seolah-olah berada dalam satu switch layer 2 yang sama melewati core provider MPLS.</li>
                <li><strong>Virtual Environment:</strong> Pengaturan routing, labeling path, dan virtual circuit dibangun seutuhnya menggunakan Virtual Machine dan server Ubuntu.</li>
            </ul>
        `
    },
    aaj: {
        title: "AAJ - Net Admin & Server",
        tag: "ADMIN NET // SERVERS",
        videoFormat: "landscape",
        body: `
            <p><strong>AAJ Project</strong> berfokus pada Administrasi Aplikasi Jaringan dengan merancang dan menguji fungsionalitas server web lokal berskala medium.</p>
            
            <h4>Fitur & Spesifikasi:</h4>
            <ul>
                <li><strong>Server Services Integration:</strong> Konfigurasi terpusat untuk DNS Server, Web Server (Apache/Nginx), Database Server, dan FTP Server.</li>
                <li><strong>Virtual Server Lab:</strong> Dibangun dan disimulasikan menggunakan server berbasis Ubuntu di dalam platform Virtual Machine untuk verifikasi akses client.</li>
            </ul>
        `
    },
    corn: {
        title: "Corn Processing Machine PLC",
        tag: "AUTOMATION // PLC // 3D",
        videoFormat: "landscape",
        body: `
            <p><strong>Corn Processing Machine Automation</strong> adalah proyek perancangan komprehensif rencana pengembangan mesin pengolah jagung otomatis skala industri.</p>
            
            <h4>Fitur & Spesifikasi:</h4>
            <ul>
                <li><strong>3D Mechanical Modeling:</strong> Merancang model fisik mesin secara detail (proses dari pengupasan kulit jagung, pemipilan, pengeringan, hingga mesin pengemas produk).</li>
                <li><strong>PLC Logic Design:</strong> Mendesain diagram tangga (ladder diagram) logika kontrol mesin industri menggunakan software CX-One / CX-Programmer.</li>
            </ul>
        `
    },
    audio: {
        title: "Audio Filter Analyzer FFT",
        tag: "DSP // MATLAB // FFT",
        videoFormat: "landscape",
        body: `
            <p><strong>Audio Filter FFT Project</strong> berfokus pada perancangan sistem analisis sinyal suara dan penyaringan (filtering) audio berbasis teknik komputasi matematika.</p>
            
            <h4>Fitur & Spesifikasi:</h4>
            <ul>
                <li><strong>Transformasi Fourier Cepat (FFT):</strong> Mengimplementasikan algoritma FFT di Matlab untuk menganalisis spektrum frekuensi audio secara real-time.</li>
                <li><strong>Perbandingan DFT vs FFT:</strong> Menganalisis efisiensi komputasi antara algoritma Discrete Fourier Transform (DFT) konvensional dengan FFT.</li>
            </ul>
        `
    },
    bluecheck: {
        title: "Bluecheck Water Quality Sensor",
        tag: "IOT // SENSOR TECH",
        videoFormat: "landscape",
        body: `
            <p><strong>Bluecheck Water Quality Sensor</strong> adalah sensor kualitas air digital presisi tinggi yang berperan sebagai node sensor mandiri di dalam ekosistem Bieon Ecosense.</p>
            
            <h4>Fitur & Spesifikasi:</h4>
            <ul>
                <li><strong>Kalibrasi Kompleks:</strong> Pengembangan sensor melalui tahap kalibrasi bertingkat menggunakan rumus regresi untuk mencocokkan pembacaan ADC dengan nilai referensi.</li>
                <li><strong>Validasi Lab:</strong> Nilai akurasi alat divalidasi langsung dengan membandingkan hasil uji menggunakan alat laboratorium kimia bersertifikasi standar industri.</li>
            </ul>
        `
    },
    moocare: {
        title: "Moocare - Mastitis Detector",
        tag: "PROFESSIONAL // COLLAB // AI",
        videoFormat: "landscape",
        body: `
            <p><strong>Moocare</strong> is a professional collaborative project creating a portable mastitis screening device using AI and Edge Computing.</p>
            
            <h4>Impact & Technical Highlights:</h4>
            <ul>
                <li><strong>Triple-Parameter Screening:</strong> Fused thermal, visual (MobileNetV2), and TDS data for highly accurate early detection.</li>
                <li><strong>100% Offline Edge Inference:</strong> Engineered the system to run completely on-site (offline) for remote agricultural environments, syncing to Firebase only when internet is restored.</li>
            </ul>
            <a href="https://github.com/JPROGIPB/Moocare-mastitis-detector" target="_blank" class="btn-primary" style="margin-top: 15px; display: inline-block;">View Repository <i class="fa-solid fa-arrow-right"></i></a>
        `
    },
    aquarium: {
        title: "AI Aquarium Cleaner Robot",
        tag: "PROFESSIONAL // 3D MODELING",
        videoFormat: "landscape",
        body: `
            <p><strong>AI Aquarium Cleaner Robot</strong> adalah proyek desain 3D modeling dan animasi pergerakan robot pembersih aquarium otomatis.</p>
            
            <h4>Fitur & Spesifikasi:</h4>
            <ul>
                <li><strong>3D modeling:</strong> Mendesain struktur mekanis robot pembersih dinding kaca aquarium di CAD.</li>
                <li><strong>Pergerakan & Animasi:</strong> Membuat animasi gerak simulasi robot menyusuri permukaan kaca untuk mendemonstrasikan cara kerja alat secara visual ke klien.</li>
            </ul>
        `
    },
    cowshed: {
        title: "Cow Shed Cleaner Robotic",
        tag: "PROFESSIONAL // 3D MODELING",
        videoFormat: "landscape",
        body: `
            <p><strong>Cow Shed Cleaner Robotic</strong> berfokus pada desain modeling 3D robot pembersih lantai kandang sapi otomatis.</p>
            
            <h4>Fitur & Spesifikasi:</h4>
            <ul>
                <li><strong>Desain Bucket Mekanis:</strong> Robot didesain memiliki mekanisme bucket penampung kotoran di bagian bawah badan robot.</li>
                <li><strong>Simulasi Kerja:</strong> Robot dirancang bergerak menyusuri koridor kandang sapi, menyapu kotoran, dan menampungnya langsung ke dalam bucket penampungan.</li>
            </ul>
        `
    }
};

function openProjectModal(projectId) {
    const modal = document.getElementById('project-modal');
    const modalContent = modal.querySelector('.modal-content');
    const contentContainer = document.getElementById('modal-project-content');
    
    if (!modal || !modalContent || !contentContainer || !projectData[projectId]) return;

    const data = projectData[projectId];
    
    // Generate Video Embed or Placeholder
    let videoSection = '';
    if (data.reelId) {
        // Embed Instagram Reel iframe with dynamic format container
        const containerClass = (data.videoFormat === 'landscape') ? 'reels-container-landscape' : 'reels-container';
        videoSection = `
            <div class="${containerClass}">
                <iframe src="https://www.instagram.com/reel/${data.reelId}/embed/" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
            </div>
            <a href="https://www.instagram.com/reel/${data.reelId}/" target="_blank" class="btn-reels-direct">
                <i class="fa-brands fa-instagram"></i> Tonton di Instagram
            </a>
        `;
    } else {
        // Static Placeholder for landscape projects without video link
        videoSection = `
            <div class="modal-video-placeholder">
                <i class="fa-solid fa-laptop-code" style="color: #c85a3c;"></i>
                <span>Video Dokumentasi Desktop (16:9)</span>
            </div>
        `;
    }

    // Reset layout classes on modal content wrapper
    modalContent.className = 'modal-content';

    // Inject content dynamically based on layout formats (UI/UX Asymmetric Layout)
    if (data.videoFormat === 'portrait') {
        // Apply split-screen layout class on desktop
        modalContent.classList.add('modal-portrait');
        
        contentContainer.innerHTML = `
            <div class="modal-split-wrapper">
                <div class="modal-left-media">
                    ${videoSection}
                </div>
                <div class="modal-right-info">
                    <div class="modal-project-header">
                        <span class="project-tag" style="font-family: 'Space Mono', monospace; font-size: 0.7rem; color: #c85a3c; font-weight: 700; letter-spacing: 0.5px; display: block; margin-bottom: 0.4rem;">
                            ${data.tag}
                        </span>
                        <h3 class="modal-project-title" style="font-family: 'Lora', serif; font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem;">
                            ${data.title}
                        </h3>
                    </div>
                    <div class="modal-body">
                        ${data.body}
                    </div>
                </div>
            </div>
        `;
    } else {
        // Standard Stacked Layout for landscape (video full-width, text below)
        modalContent.classList.add('modal-landscape');
        
        contentContainer.innerHTML = `
            <div class="modal-project-header">
                <span class="project-tag" style="font-family: 'Space Mono', monospace; font-size: 0.7rem; color: #c85a3c; font-weight: 700; letter-spacing: 0.5px; display: block; margin-bottom: 0.4rem;">
                    ${data.tag}
                </span>
                <h3 class="modal-project-title" style="font-family: 'Lora', serif; font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem;">
                    ${data.title}
                </h3>
            </div>
            ${videoSection}
            <div class="modal-body" style="max-height: 250px;">
                ${data.body}
            </div>
        `;
    }

    // Show modal
    modal.classList.add('active');
    document.body.style.overflow = 'hidden'; // Lock background scrolling
}

function closeProjectModal() {
    const modal = document.getElementById('project-modal');
    if (!modal) return;
    
    modal.classList.remove('active');
    document.body.style.overflow = ''; // Restore scrolling
    
    // Destroy content on close to stop video/audio playing in background
    const contentContainer = document.getElementById('modal-project-content');
    if (contentContainer) {
        contentContainer.innerHTML = '';
    }
}

// Close modal when clicking on the backdrop
const modalBackdrop = document.getElementById('project-modal');
if (modalBackdrop) {
    modalBackdrop.addEventListener('click', function(e) {
        if (e.target === modalBackdrop) {
            closeProjectModal();
        }
    });
}


// ==========================================================================
// ACTIVE NAV LINK & HEADER SCROLL EFFECT
// ==========================================================================
window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('section[id], aside[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    const header = document.querySelector('.header');
    
    // Header class toggle based on scroll position
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
    
    let currentId = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (window.scrollY >= (sectionTop - 150)) {
            currentId = section.getAttribute('id');
        }
    });

    if (currentId) {
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').slice(1) === currentId) {
                link.classList.add('active');
            }
        });
    }
});


// ==========================================================================
// PORTFOLIO FILTER SYSTEM & HEADER INITIALIZATION
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
    const header = document.querySelector('.header');
    if (header && window.scrollY > 50) {
        header.classList.add('scrolled');
    }

    const filterButtons = document.querySelectorAll('.filter-btn');
    const portfolioCards = document.querySelectorAll('.portfolio-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            button.classList.add('active');

            const filterValue = button.getAttribute('data-filter');

            portfolioCards.forEach(card => {
                const cardCategory = card.getAttribute('data-category');
                
                if (filterValue === 'all' || cardCategory === filterValue) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
        });
    });
});

    // ==========================================================================
// SCROLL ANIMATIONS (INTERSECTION OBSERVER)
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll('.animate-on-scroll');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            const animationClass = entry.target.getAttribute('data-animation') || 'animate-pop-up';
            if (entry.isIntersecting) {
                entry.target.classList.add(animationClass);
            } else {
                entry.target.classList.remove(animationClass);
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    });

    animatedElements.forEach((el) => observer.observe(el));
});

document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('seeAllCertsBtn');
    if (btn) {
        btn.addEventListener('click', () => {
            const hiddenCerts = document.querySelectorAll('.hidden-cert');
            hiddenCerts.forEach(cert => cert.classList.toggle('cert-show'));
            if (btn.innerText === 'View All Certificates') {
                btn.innerText = 'Show Less';
            } else {
                btn.innerText = 'View All Certificates';
            }
        });
    }
});



// ==========================================================================
// TYPING ANIMATION (ABOUT SECTION)
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
    const typingSpan = document.getElementById('typing-text');
    if (!typingSpan) return;

    // Decode HTML entities
    const rawHtml = typingSpan.getAttribute('data-html') || '';
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = rawHtml;
    const fullHtml = tempDiv.innerHTML;

    let i = 0;
    let isTyping = false;
    let typeInterval;

    const typeWriter = () => {
        if (i < fullHtml.length) {
            // Handle HTML tags: if we hit a '<', find the closing '>'
            if (fullHtml.charAt(i) === '<') {
                const closeTag = fullHtml.indexOf('>', i);
                if (closeTag !== -1) {
                    typingSpan.innerHTML += fullHtml.substring(i, closeTag + 1);
                    i = closeTag + 1;
                }
            } else {
                typingSpan.innerHTML += fullHtml.charAt(i);
                i++;
            }
            typeInterval = setTimeout(typeWriter, 20); // typing speed
        }
    };

    // Use Intersection Observer to trigger typing when scrolled into view
    const aboutObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                if (!isTyping) {
                    isTyping = true;
                    typingSpan.innerHTML = '';
                    i = 0;
                    typeWriter();
                }
            } else {
                // Reset when scrolled out of view to re-trigger consistently
                clearTimeout(typeInterval);
                typingSpan.innerHTML = '';
                i = 0;
                isTyping = false;
            }
        });
    }, {
        threshold: 0.5
    });

    const aboutSection = document.getElementById('about');
    if (aboutSection) {
        aboutObserver.observe(aboutSection);
    }
});
