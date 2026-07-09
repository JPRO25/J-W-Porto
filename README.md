# Website Portofolio Editorial Cerah (Light Mode) - Julman Waruwu

Website portofolio ini didesain secara khusus untuk merepresentasikan keahlian multi-disiplin Anda di bidang **IoT, Embedded Systems, AIoT, Web Development, dan 3D Design (CAD)** dengan tata letak **asimetris editorial** yang bersih dan tidak terkesan kaku seperti template biasa.

---

## 📁 Struktur Folder Aset Baru

Aset-aset penting Anda dapat dimasukkan ke dalam folder terorganisir berikut:
*   `assets/images/` -> Simpan foto profil Anda (misal: `pp.jpg`) dan foto sertifikasi kompetensi.
*   `assets/videos/` -> Simpan file demo video lokal (jika diperlukan).
*   `assets/docs/` -> Simpan dokumen CV/Resume dalam format PDF (misal: `CV_Julman_Waruwu.pdf`).
*   `assets/3d/` -> Simpan gambar tangkapan layar render 3D CAD kustom Anda dari Fusion 360/SolidWorks.

---

## 🎬 Integrasi Instagram Reels (Memutar Video di Website)

Jika video dokumentasi proyek Anda dipublikasikan di Instagram Reels, Anda dapat memutarnya langsung di dalam modal pop-up website ini.

### Cara Mendapatkan ID Instagram Reel Anda:
1. Buka video Reels Anda di browser (desktop atau HP).
2. Lihat alamat URL video tersebut. Formatnya akan seperti:
   `https://www.instagram.com/reel/C7-xxxxxx/` atau `https://www.instagram.com/p/C7-xxxxxx/`
3. Kode acak di antara kata `/reel/` dan tanda garis miring terakhir (dalam contoh ini: **`C7-xxxxxx`**) adalah **Reel ID** Anda.

### Cara Memasukkan ke Website:
1. Buka file `script.js`.
2. Cari objek `projectData` di bagian paling atas.
3. Pada proyek yang ingin Anda hubungkan dengan Reels (misalnya `bieon`, `rover`, `cad3d`, atau `tinymlcam`), ganti nilai properti `reelId` dengan kode ID Reel Anda sendiri:
   ```javascript
   bieon: {
       title: "BIEON - Smart Automation Ecosystem",
       tag: "Smart System Ecosystem",
       reelId: "C7-xxxxxx", // Ganti dengan ID Reel asli Anda
       body: `...`
   }
   ```
4. Simpan file `script.js`. Website akan memuat pemutar Reels secara otomatis saat kartu proyek diklik!

---

## 🚀 Cara Menjalankan Proyek Secara Lokal

Cukup jalankan server statis lokal:

### Opsi 1: Menggunakan Ekstensi VS Code (Sangat Direkomendasikan)
1. Buka folder `personal-portfolio` ini di editor kode Anda.
2. Instal ekstensi **Live Server** di VS Code.
3. Klik tombol **"Go Live"** di pojok kanan bawah editor untuk langsung membukanya di browser Anda.

### Opsi 2: Menggunakan Terminal Python (Bawaan Windows)
Buka terminal/PowerShell di direktori ini dan jalankan:
```bash
python -m http.server 8000
```
Lalu buka browser Anda dan akses `http://localhost:8000`.

---

> [!TIP]
> **Rekomendasi Workspace:** Setel folder `C:\Users\Julman Waruwu\.gemini\antigravity-ide\scratch\personal-portfolio` ini sebagai **Workspace Aktif** di editor Anda agar mempermudah navigasi.
