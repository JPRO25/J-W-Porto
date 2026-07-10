import os

html_template = '''<!DOCTYPE html>
<html lang="{lang_code}">
<head>
    <meta charset="UTF-8">
    <title>Julman Notatema Waruwu - ATS Resume</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            color: #000;
            line-height: 1.4;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px;
            background: #fff;
        }}
        h1 {{
            font-size: 24px;
            text-align: center;
            text-transform: uppercase;
            margin-bottom: 5px;
            letter-spacing: 1px;
        }}
        .contact-info {{
            text-align: center;
            font-size: 13px;
            margin-bottom: 20px;
        }}
        .contact-info a {{
            color: #000;
            text-decoration: none;
        }}
        h2 {{
            font-size: 14px;
            text-transform: uppercase;
            border-bottom: 1px solid #000;
            padding-bottom: 3px;
            margin-top: 20px;
            margin-bottom: 10px;
            letter-spacing: 0.5px;
        }}
        p {{
            font-size: 13px;
            margin-top: 0;
            margin-bottom: 10px;
            text-align: justify;
        }}
        ul {{
            margin-top: 0;
            margin-bottom: 10px;
            padding-left: 20px;
        }}
        li {{
            font-size: 13px;
            margin-bottom: 4px;
        }}
        .item-header {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 2px;
        }}
        .item-title {{
            font-weight: bold;
            font-size: 13px;
        }}
        .item-date {{
            font-size: 13px;
            font-style: italic;
        }}
        .item-subtitle {{
            font-style: italic;
            font-size: 13px;
            margin-bottom: 5px;
            font-weight: bold;
        }}
        .skills-grid {{
            display: grid;
            grid-template-columns: 220px 1fr;
            gap: 5px;
            font-size: 13px;
            margin-bottom: 10px;
        }}
        .skill-category {{
            font-weight: bold;
        }}
        .repo-links {{
            font-size: 13px;
            margin-bottom: 10px;
        }}
        .repo-links a {{
            color: #000;
        }}
        @media print {{
            body {{
                padding: 0;
            }}
        }}
    </style>
</head>
<body>

    <h1>Julman Notatema Waruwu</h1>
    <div class="contact-info">
        Bogor, Indonesia | +62 853-5886-2982 | <a href="mailto:jul2005war@gmail.com">jul2005war@gmail.com</a><br>
        <a href="https://jprogipb.github.io/">jprogipb.github.io</a> | <a href="https://linkedin.com/in/julwar005">linkedin.com/in/julwar005</a> | <a href="https://github.com/JPROGIPB">github.com/JPROGIPB</a>
    </div>

    <h2>{sec_summary}</h2>
    <p>{summary_text}</p>

    <h2>{sec_skills}</h2>
    <div class="skills-grid">
        <div class="skill-category">{lbl_lang}:</div>
        <div>C/C++, Python, JavaScript</div>
        <div class="skill-category">Embedded Systems & IoT:</div>
        <div>ESP32, ESP-IDF, Arduino, Raspberry Pi 4, PlatformIO, ESP-NOW, MQTT, Sensor Integration</div>
        <div class="skill-category">Artificial Intelligence (AI):</div>
        <div>TinyML, Cloud AI Inference, Computer Vision, Reinforcement Learning, Random Forest, LLM Integration</div>
        <div class="skill-category">Cloud & Networking:</div>
        <div>AWS IoT Core, Firebase, WebSocket, HTTP/HTTPS, MongoDB, Wireshark, Nmap</div>
        <div class="skill-category">Web Development:</div>
        <div>React.js, Node.js, Flask API, REST API Development</div>
        <div class="skill-category">{lbl_mech}:</div>
        <div>Fusion 360, Custom PCB Design, 3D Printing, CAD Modeling</div>
    </div>

    <h2>{sec_experience}</h2>

    <div class="item-header">
        <div class="item-title">IoT Engineering Intern (Bieon Project Lead) | PT Matra Kreasi Mandiri</div>
        <div class="item-date">Feb 2026 – Jun 2026</div>
    </div>
    <ul>
        <li>{exp1_1}</li>
        <li>{exp1_2}</li>
        <li>{exp1_3}</li>
    </ul>

    <div class="item-header">
        <div class="item-title">Embedded Systems Specialist | Automation Solution Lab</div>
        <div class="item-date">2024</div>
    </div>
    <ul>
        <li>{exp2_1}</li>
        <li>{exp2_2}</li>
        <li>{exp2_3}</li>
    </ul>

    <div class="item-header">
        <div class="item-title">IoT & Web Developer (Freelance) | Independent Services</div>
        <div class="item-date">2023</div>
    </div>
    <ul>
        <li>{exp3_1}</li>
        <li>{exp3_2}</li>
        <li>{exp3_3}</li>
    </ul>

    <h2>{sec_projects}</h2>

    <div class="item-header">
        <div class="item-title">SEALEN - AI-Powered Autonomous Beach Cleaning Robot</div>
        <div class="item-date">Sep 2025 – Dec 2025</div>
    </div>
    <div class="item-subtitle">Team Leader | {lbl_academic}</div>
    <ul>
        <li>{proj1_1}</li>
        <li>{proj1_2}</li>
        <li>{proj1_3}</li>
    </ul>

    <div class="item-header">
        <div class="item-title">PresentHub - Smart Attendance & Health Monitoring System</div>
        <div class="item-date">Mar 2025 – Jun 2025</div>
    </div>
    <div class="item-subtitle">Team Leader | {lbl_independent}</div>
    <ul>
        <li>{proj2_1}</li>
        <li>{proj2_2}</li>
        <li>{proj2_3}</li>
    </ul>

    <div class="item-header">
        <div class="item-title">Moocare - Mastitis Detector</div>
        <div class="item-date">2025</div>
    </div>
    <div class="item-subtitle">AI & Edge Computing Integrator | {lbl_research}</div>
    <ul>
        <li>{proj3_1}</li>
        <li>{proj3_2}</li>
    </ul>

    <div class="item-header">
        <div class="item-title">Your Path - AI CV Analyzer</div>
        <div class="item-date">2026</div>
    </div>
    <div class="item-subtitle">Data Science & AI Integrator | Dicoding Camp DBS Foundation</div>
    <ul>
        <li>{proj4_1}</li>
        <li>{proj4_2}</li>
    </ul>

    <h2>{sec_education}</h2>
    <div class="item-header">
        <div class="item-title">D4 {lbl_major}</div>
        <div class="item-date">2023 – {present}</div>
    </div>
    <div class="item-subtitle">IPB University, Indonesia</div>

    <h2>{sec_certs}</h2>
    <ul>
        <li><strong>Applied Machine Learning Specialist</strong> – Dicoding Indonesia (2026)</li>
        <li><strong>Fullstack Web Developer (React & Node.js)</strong> – Dicoding Indonesia (2026)</li>
        <li><strong>Edge AI & TinyML Developer Specialist</strong> – Google Cloud (2025)</li>
        <li><strong>Cybersecurity Essentials Specialist</strong> – Cisco Networking Academy (2025)</li>
        <li><strong>3D Modeling & Mechanical Design (Fusion 360)</strong> – Autodesk (2024)</li>
        <li><strong>Low-Touch Programming</strong> – Coding Camp powered by DBS Foundation (2025)</li>
        <li><strong>Cloud Computing & Backend Services</strong> – AWS Back-End Academy</li>
    </ul>

    <h2>{sec_org}</h2>
    <ul>
        <li><strong>IdeaFest 2025:</strong> {lbl_comp1} (2025)</li>
        <li><strong>{lbl_comp2}:</strong> {lbl_comp3} (2025)</li>
        <li><strong>United Tractor Digital Hackathon 2025:</strong> Digital Innovation (2025)</li>
        <li><strong>OLIVIA 2025:</strong> Smart System / IoT (2025)</li>
    </ul>

</body>
</html>
'''

data_id = {
    'lang_code': 'id',
    'sec_summary': 'Ringkasan Profesional',
    'summary_text': 'Smart Systems Engineer dan Fullstack Developer dengan fokus pada Internet of Things (IoT), Integrasi Cloud AI, dan Sistem Tertanam. Memiliki keahlian end-to-end mulai dari perancangan arsitektur, desain custom PCB, programming mikrokontroler (C++/Python), hingga integrasi cloud dan dashboard web (React.js/Node.js). Terbukti memimpin tim lintas disiplin dalam mengembangkan robot otonom dan otomasi industri yang berhasil memangkas waktu operasional dan biaya secara terukur. Mengombinasikan logika engineer dengan eksekusi cepat untuk memberikan solusi teknis yang scalable dan inovatif.',
    'sec_skills': 'Keahlian Teknis',
    'lbl_lang': 'Bahasa Pemrograman',
    'lbl_mech': 'Mekanik & Desain Industri',
    'sec_experience': 'Pengalaman Profesional',
    'present': 'Sekarang',
    
    'exp1_1': 'Merancang penuh sirkuit custom PCB dan memprogram firmware C++ pada ESP32, mengurangi noise sinyal hardware secara signifikan.',
    'exp1_2': 'Mengkonfigurasi transmisi data nirkabel menggunakan ESP-NOW dan MQTT, menjaga stabilitas 5+ node sensor tanpa packet loss.',
    'exp1_3': 'Membangun dashboard web pemantauan terpusat berbasis React.js yang menurunkan latensi pengiriman data hingga di bawah 1 detik (sub-second latency).',
    
    'exp2_1': 'Mendesain prototipe casing 3D kustom (CAD) dengan struktur snap-fit, menghemat biaya produksi casing hingga 30% menggunakan teknik 3D printing.',
    'exp2_2': 'Mengintegrasikan pipeline model AI dengan sistem IoT untuk memproses data sensor dan visual secara cloud/backend, mencapai akurasi inferensi >90%.',
    'exp2_3': 'Mengintegrasikan database lokal dan gateway jaringan untuk mengamankan data industri sebelum ditransmisikan ke cloud.',
    
    'exp3_1': 'Mengembangkan 3+ sistem otomatisasi cerdas (Arduino/ESP32) untuk klien UMKM dan akademis.',
    'exp3_2': 'Mengotomatisasi pipeline pengiriman data sensor ke cloud Firebase, menekan waktu pelaporan manual klien hingga 40%.',
    'exp3_3': 'Membangun dashboard visualisasi data sensor yang interaktif berbasis React.js untuk mempermudah monitoring jarak jauh.',
    
    'sec_projects': 'Proyek Engineering Terpilih',
    'lbl_academic': 'Proyek Akademik Lintas-Disiplin',
    'lbl_independent': 'Proyek Engineering Independen',
    'lbl_research': 'Proyek Riset Kolaboratif',
    
    'proj1_1': 'Merancang robot pembersih perairan otonom menggunakan Raspberry Pi 4, motor controller, dan sensor lingkungan.',
    'proj1_2': 'Menerapkan algoritma Reinforcement Learning (RL) untuk navigasi, meningkatkan efisiensi pembersihan perairan dangkal sebesar 60% dibanding metode manual.',
    'proj1_3': 'Mengembangkan strategi sensor fusion dan Computer Vision untuk meningkatkan akurasi deteksi objek sampah plastik hingga 85%.',
    
    'proj2_1': 'Mengintegrasikan modul ESP32-CAM untuk sistem face recognition real-time yang memangkas waktu absensi kelas dari 15 menit menjadi di bawah 3 menit (peningkatan kecepatan 80%).',
    'proj2_2': 'Mengimplementasikan sensor MLX90614 dan mekanisme anti-spoofing untuk memastikan keaslian kehadiran dengan tingkat akurasi 95%.',
    'proj2_3': 'Menyinkronkan data kehadiran dan suhu tubuh ke database Firebase secara real-time yang dapat diakses melalui web dashboard.',
    
    'proj3_1': 'Mengembangkan alat screening penyakit mastitis sapi berbasis IoT yang mentransmisikan data lingkungan peternakan ke server untuk dianalisis oleh AI.',
    'proj3_2': 'Mencapai akurasi deteksi awal 85% dengan memadukan sensor suhu (thermal), klasifikasi AI visual dari citra susu, dan metrik TDS.',
    
    'proj4_1': 'Memproses 100+ sampel data latih dan membangun model klasifikasi kelayakan CV menggunakan Random Forest dengan akurasi 92%.',
    'proj4_2': 'Mengintegrasikan pipeline dengan Large Language Models (LLM) untuk secara otomatis merangkum hasil klasifikasi dan menghasilkan rekomendasi karir presisi.',
    
    'sec_education': 'Pendidikan',
    'lbl_major': 'Teknologi Rekayasa Komputer',
    'sec_certs': 'Sertifikasi',
    'sec_org': 'Kompetisi',
    'lbl_comp1': 'Teknologi dan Pangan',
    'lbl_comp2': 'Lomba Riset BPDPKS 2025',
    'lbl_comp3': 'Teknologi dan AI'
}

data_en = {
    'lang_code': 'en',
    'sec_summary': 'Professional Summary',
    'summary_text': 'Smart Systems Engineer and Fullstack Developer specializing in the Internet of Things (IoT), Cloud AI Integration, and Embedded Systems. Possesses end-to-end expertise spanning from architectural planning, custom PCB design, and microcontroller programming (C++/Python), to cloud integration and web dashboard development (React.js/Node.js). Proven track record of leading cross-functional teams in developing autonomous robots and industrial automation, successfully reducing operational times and costs with measurable metrics. Combines engineering rigor with rapid execution to deliver highly scalable and innovative technical solutions.',
    'sec_skills': 'Technical Skills',
    'lbl_lang': 'Programming Languages',
    'lbl_mech': 'Mechanical & Industrial Design',
    'sec_experience': 'Professional Experience',
    'present': 'Present',
    
    'exp1_1': 'Designed custom PCB circuits and programmed C++ firmware on the ESP32, significantly reducing hardware signal noise.',
    'exp1_2': 'Configured wireless data transmission protocols via ESP-NOW and MQTT, maintaining high stability across 5+ sensor nodes without packet loss.',
    'exp1_3': 'Built a centralized, React.js-based web monitoring dashboard that decreased data transmission latency to under 1 second (sub-second latency).',
    
    'exp2_1': 'Designed 3D-printed custom casing prototypes (CAD) featuring snap-fit structures, cutting production costs by 30%.',
    'exp2_2': 'Integrated AI model pipelines with IoT systems to process sensor and visual data via cloud/backend, achieving >90% inference accuracy.',
    'exp2_3': 'Integrated local databases and network gateways to secure industrial data prior to cloud transmission.',
    
    'exp3_1': 'Developed 3+ smart automation systems (Arduino/ESP32) for MSMEs and academic clients.',
    'exp3_2': 'Automated sensor data pipelines to Firebase, reducing manual client reporting time by an average of 40%.',
    'exp3_3': 'Built interactive sensor data visualization dashboards using React.js to streamline remote monitoring processes.',
    
    'sec_projects': 'Selected Engineering Projects',
    'lbl_academic': 'Cross-Disciplinary Academic Project',
    'lbl_independent': 'Independent Engineering Project',
    'lbl_research': 'Collaborative Research Project',
    
    'proj1_1': 'Designed an autonomous marine cleaning robot utilizing Raspberry Pi 4, motor controllers, and environmental sensors.',
    'proj1_2': 'Implemented Reinforcement Learning (RL) for navigation, boosting shallow-water cleaning efficiency by 60% compared to manual methods.',
    'proj1_3': 'Developed sensor fusion and Computer Vision strategies to improve plastic waste object detection accuracy to 85%.',
    
    'proj2_1': 'Integrated the ESP32-CAM module for a real-time face recognition system that slashed class attendance time from 15 minutes to under 3 minutes (80% speed increase).',
    'proj2_2': 'Implemented an MLX90614 sensor and anti-spoofing mechanisms to ensure attendance authenticity with 95% accuracy.',
    'proj2_3': 'Synchronized attendance and body temperature data to a Firebase real-time database, accessible via a web dashboard.',
    
    'proj3_1': 'Developed a portable mastitis screening device for dairy cows utilizing IoT to transmit farm environmental data to a cloud/backend server for AI analysis.',
    'proj3_2': 'Achieved an 85% early detection accuracy by combining thermal sensors, visual AI classification from milk imagery, and TDS metrics.',
    
    'proj4_1': 'Processed 100+ training data samples and built a CV feasibility classification model using Random Forest with 92% accuracy.',
    'proj4_2': 'Integrated the pipeline with Large Language Models (LLM) to automatically summarize classification results and generate precision career recommendations.',
    
    'sec_education': 'Education',
    'lbl_major': 'Computer Engineering Technology (B.App.Sc)',
    'sec_certs': 'Certifications',
    'sec_org': 'Competitions',
    'lbl_comp1': 'Technology & Food',
    'lbl_comp2': 'BPDPKS Research Competition 2025',
    'lbl_comp3': 'Technology & AI'
}

with open('CV_ATS_Julman_Waruwu_ID.html', 'w', encoding='utf-8') as f:
    f.write(html_template.format(**data_id))
    
with open('CV_ATS_Julman_Waruwu.html', 'w', encoding='utf-8') as f:
    f.write(html_template.format(**data_en))

print('Successfully generated ATS CVs')
