# PANDUAN PENJELASAN DASHBOARD WEB
**Riset NDAC EPSILON 2026: Kuantitas Tanpa Kualitas**
*Mirza Muhyidin & Faiz Iqbal I'tishom — Universitas Airlangga*

---

## 1. Bagian Header & Ringkasan Eksekutif (Hero Section)

### A. Judul & Latar Belakang Riset
* **Poin Penjelasan:** Dashboard ini memvisualisasikan karya analisis spasial-panel terkait determinan Angka Harapan Hidup (AHH) di 38 provinsi Indonesia.
* **Tesis Inti:** Angka penyerapan kerja tinggi di Indonesia bersifat semu. Bekerja di sektor informal berproduktivitas rendah bukan tanda sejahtera, melainkan keterpaksaan bertahan hidup (*working poor*), yang justru mengikis modal kesehatan fisik.

### B. 4 Kartu Indikator Kunci (KPI Cards)
1. **Disparitas AHH 2024 (10,77 tahun):**
   * Jurang ketimpangan usia harapan hidup tertinggi (DI Yogyakarta: 75,53 tahun) vs terendah (Papua Pegunungan: 64,76 tahun).
2. **Paradoks Ketenagakerjaan (98,68%):**
   * Papua Pegunungan memegang rekor tingkat kerja tertinggi nasional, namun harapan hidupnya paling rendah se-Indonesia.
3. **Multiplier Limpahan (4,12×):**
   * Rasio efek limpahan PDRB ke provinsi sekitar (2,138) dibanding efek lokal yang tertahan di provinsi asal (0,519).
4. **Koefisien Tingkat Kerja SDM (-0,0286*):**
   * Setelah lag spasial dikendalikan, kuantitas kerja terbukti bertanda negatif signifikan terhadap AHH. Konsisten non-positif di 7 spesifikasi model ekonometrika.

---

## 2. Bagian Peta Spasial Vektor Interaktif (Choropleth Map)

### A. Filter Indikator Tematik (Tab Peta)
* **AHH (Tahun):** Menampilkan ketimpangan geografis barat-timur. Klaster tinggi terpusat di Jawa/Bali, klaster rendah di kawasan timur (Moran's I = 0,348, p = 0,004).
* **Tingkat Kerja (%):** Sebaran homogen semu (SD hanya 1,41%), membuktikan penyerapan kerja tidak mengikuti pola kesejahteraan kesehatan.
* **PDRB per Kapita:** Sebaran acak spasial (Moran's I = -0,061, tidak signifikan) akibat kantong enklave tambang terisolasi.
* **Residual Spasial:** Menampilkan anomali lokal model:
  * **Merah (Underperformer):** Daerah yang AHH-nya jauh di bawah potensi ekonominya (Papua Barat -3,80 th, Sulbar -3,24 th).
  * **Hijau (Overperformer):** Daerah yang AHH-nya jauh melampaui kapasitas ekonominya (DIY +3,38 th).

### B. Fitur Tooltip Hover (Tanpa Klik)
* Saat kursor diarahkan ke poligon provinsi mana saja, tooltip instan menampilkan 4 data riil:
  1. Nama Provinsi
  2. AHH (Tahun)
  3. Tingkat Kerja (%)
  4. PDRB per Kapita (Rp Juta)
  5. Residual Model SDM (Tahun deviasi)

### C. Pembuktian Matriks Bobot Spasial W (KNN k=4)
* **Aksi:** Klik provinsi mana saja (misal: Papua Pegunungan, Maluku, atau Bali).
* **Visualisasi:** Otomatis muncul 4 garis busur putus-putus (*spatial arcs*) ke 4 tetangga terdekat.
* **Argumen Metodologis:**
  * Di negara kepulauan, metode batas darat (*contiguity*) gagal karena pulau seperti Maluku/Kepri tidak punya perbatasan darat (baris matriks kosong).
  * Pendekatan K-Nearest Neighbors (k=4) menjamin interkoneksi spasial 100% kontinu tanpa jeda batas laut.

---

## 3. Bagian Panel Detail Provinsi (Sidebar Kanan Peta)

Menampilkan profil lengkap provinsi yang sedang disorot beserta 3 studi kasus utama:

1. **Papua Pegunungan (Kasus Paradoks Kerja):**
   * Tingkat kerja 98,68%, AHH 64,76 tahun, PDRB per kapita Rp 18,1M.
   * *Makna:* Bekerja fisik berat jam panjang demi makan di tengah minimnya faskes dasar.
2. **Papua Barat (Kasus Kutukan Sumber Daya Alam / Dutch Disease):**
   * Residual negatif terbesar: **-3,80 tahun** di bawah prediksi model.
   * *Makna:* PDRB tinggi semu dari enklave migas LNG Tangguh. Terjadi kebocoran pendapatan (*revenue leakage* ke luar daerah), minim penyerapan naker lokal, dan degradasi lingkungan.
3. **DI Yogyakarta (Kasus Efisiensi Modal Sosial):**
   * Residual positif terbesar: **+3,38 tahun** di atas prediksi model.
   * *Makna:* PDRB menengah tanpa tambang, namun AHH tertinggi nasional berkat modal sosial guyub, posyandu lansia aktif, dan rasio dokter primer merata.

---

## 4. Bagian Kalkulator Dekomposisi Efek Spasial (LeSage & Pace, 2009)

### A. Formulasi Matematis
$$\frac{\partial Y}{\partial X_k} = (I - \rho W)^{-1} (\beta_k I + \theta_k W)$$
$$\text{Spatial Multiplier} = \frac{1}{1 - \rho} = \frac{1}{1 - 0,6126} = \mathbf{2,581\times}$$

### B. Interaktivitas Slider
* Slider $\rho$ (lag dependen), $\beta$ (koefisien lokal), dan $\theta$ (koefisien tetangga) dapat digeser untuk mensimulasikan perubahan struktur spasial secara real-time.

### C. Dekomposisi Hasil Estimasi
* **Efek Langsung (Direct Effect) = +0,519:**
  * Dampak internal PDRB per kapita yang dinikmati provinsi itu sendiri.
* **Efek Limpahan (Indirect Spillover) = +2,138:**
  * Akumulasi dampak kemakmuran yang meluap ke seluruh provinsi tetangga (4,12 kali lipat efek lokal).
* **Efek Total = +2,657:**
  * Total dampak agregat nasional dari peningkatan PDRB.

### D. Implikasi Kebijakan
* Karena manfaat kesehatan lebih banyak mengalir melintasi batas administratif (rujukan rumah sakit, mobilitas tenaga medis, distribusi obat), **kebijakan pembangunan kesehatan tidak boleh dibuat terisolasi per provinsi, melainkan wajib berbasis kawasan terkoordinasi**.
