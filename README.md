# Kuantitas Tanpa Kualitas — Spatial Econometric Research Hub

Repositori resmi penelitian **National Data Analysis Competition (NDAC) — EPSILON 2026** oleh Mirza Muhyidin & Faiz Iqbal I'tishom (Departemen Statistika, Universitas Airlangga).

## 📌 Ringkasan Riset
- **Judul:** Kuantitas Tanpa Kualitas: Pemodelan Spasial-Panel Penggerak Ekonomi terhadap Angka Harapan Hidup Provinsi di Indonesia (2013–2024)
- **Metode Utama:** Spatial Durbin Model (SDM) Fixed Effects, K-Nearest Neighbors (KNN $k=4$) Row-Standardized, Dekomposisi Efek LeSage & Pace (2009).
- **Temuan Kunci:**
  1. Kuantitas kerja (Tingkat Kerja) bertanda negatif signifikan ($-0.0286*$) setelah mengontrol lag spasial, konsisten dengan konsep *Working Poor* (ILO) & depresiasi modal kesehatan (Grossman).
  2. Efek limpahan (*indirect spillover*) PDRB per kapita ke provinsi tetangga ($2.138$) mencapai **4,12 kali lipat** dari efek langsung yang tertahan lokal ($0.519$).
  3. Terjadi konvergensi sigma ($-0.019$ th/th) dan konvergensi beta ($-0.252, p < 0.001$).

---

## 🚀 Live Demo & Deployment
Website ini dirancang statis dan mandiri (*standalone single-page application*), siap di-deploy langsung ke **GitHub Pages** atau **Vercel**:

### Deploy ke GitHub Pages:
1. Buat repository baru di GitHub bernama `lomba_ndac` (atau sesuai keinginan).
2. Di terminal folder ini:
   ```bash
   git init
   git add .
   git commit -m "feat: initial commit ndac epsilon 2026 website"
   git branch -M main
   git remote add origin https://github.com/<username>/<repo-name>.git
   git push -u origin main
   ```
3. Masuk ke **Settings > Pages > Branch: main / root > Save**. Website langsung live!

---

## 📂 Struktur File
```
C:/personal_mirza/lomba_ndac/
├── index.html                     # Halaman utama (Hero, Peta Leaflet 38 Provinsi, Kalkulator LeSage-Pace)
├── provinces_merged.geojson       # Batas administrasi 38 provinsi Indonesia + data empiris 2024
├── indonesia-38-provinces.geojson # Raw batas administrasi 38 provinsi
├── build_site.py                  # Script builder/generator
└── README.md                      # Dokumentasi teknis & cara deploy
```
