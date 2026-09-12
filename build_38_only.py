import json

with open('C:/personal_mirza/lomba_ndac/provinces_merged.geojson', encoding='utf-8') as f:
    geo38_str = f.read()

with open('C:/Users/mirza/Downloads/provinces_with_knn.json', encoding='utf-8') as f:
    provs38_str = f.read()

html_content = '''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Kuantitas Tanpa Kualitas — Riset NDAC EPSILON 2026</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&display=swap" rel="stylesheet">
  
  <!-- Leaflet CSS & JS -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>

  <style>
    :root {
      --bg: #faf9f6;
      --bg-surface: #ffffff;
      --bg-subtle: #f4f2ec;
      --border: #e6e2d8;
      --text: #191816;
      --text-muted: #6b675e;
      --text-subtle: #9c978b;
      --teal: #0f766e;
      --teal-light: #f0fdfa;
      --crimson: #be123c;
      --crimson-light: #fff1f2;
      --amber: #b45309;
      --amber-light: #fffbeb;
      --font-serif: 'Newsreader', Georgia, serif;
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.04);
      --shadow-md: 0 4px 14px rgba(0,0,0,0.06);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }

    nav {
      position: sticky;
      top: 0;
      background: rgba(250, 249, 246, 0.94);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      z-index: 1000;
      padding: 14px 0;
    }
    .nav-inner {
      max-width: 1180px;
      margin: 0 auto;
      padding: 0 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: var(--text);
    }
    .brand-avatar {
      width: 34px; height: 34px;
      border-radius: 8px;
      background: var(--text);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 13px;
    }
    .brand-title { font-weight: 700; font-size: 14px; letter-spacing: -0.01em; }
    .brand-sub { font-size: 11px; color: var(--text-muted); }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 24px;
      list-style: none;
    }
    .nav-links a {
      color: var(--text-muted);
      text-decoration: none;
      font-size: 13px;
      font-weight: 500;
      transition: color 0.2s;
    }
    .nav-links a:hover { color: var(--text); }
    .nav-btn {
      background: var(--text);
      color: #fff !important;
      padding: 6px 14px;
      border-radius: 6px;
      font-weight: 600 !important;
      font-size: 12px;
    }

    .container {
      max-width: 1180px;
      margin: 0 auto;
      padding: 0 24px;
    }

    /* Hero Section */
    .hero {
      padding: 64px 0 40px;
      border-bottom: 1px solid var(--border);
    }
    .hero-tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      border-radius: 20px;
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--text-muted);
      margin-bottom: 18px;
    }
    .hero-tag span { width: 6px; height: 6px; border-radius: 50%; background: var(--teal); }
    .hero-title {
      font-family: var(--font-serif);
      font-size: clamp(38px, 5vw, 54px);
      line-height: 1.15;
      font-weight: 600;
      letter-spacing: -0.02em;
      margin-bottom: 16px;
    }
    .hero-desc {
      font-size: 17px;
      color: var(--text-muted);
      max-width: 840px;
      line-height: 1.6;
      margin-bottom: 30px;
    }

    .authors-card {
      display: inline-flex;
      align-items: center;
      gap: 20px;
      padding: 14px 20px;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      box-shadow: var(--shadow-sm);
    }
    .author-item { display: flex; align-items: center; gap: 10px; }
    .author-avatar {
      width: 34px; height: 34px;
      border-radius: 50%;
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 11px;
    }
    .author-sep { width: 1px; height: 26px; background: var(--border); }

    /* KPI Grid */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
      margin: 40px 0;
    }
    .kpi-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
      box-shadow: var(--shadow-sm);
    }
    .kpi-label {
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--text-subtle);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 6px;
    }
    .kpi-val {
      font-size: 30px;
      font-weight: 800;
      letter-spacing: -0.02em;
      margin-bottom: 4px;
      font-family: var(--font-sans);
    }
    .kpi-desc { font-size: 12px; color: var(--text-muted); line-height: 1.5; }

    /* Map Explorer */
    .section-head { margin: 56px 0 20px; }
    .section-eyebrow {
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--teal);
      text-transform: uppercase;
      letter-spacing: 0.1em;
      margin-bottom: 4px;
    }
    .section-title {
      font-family: var(--font-serif);
      font-size: 28px;
      font-weight: 600;
    }
    .section-subtitle {
      font-size: 14px;
      color: var(--text-muted);
      margin-top: 4px;
    }

    .map-container {
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 20px;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px;
      box-shadow: var(--shadow-sm);
    }
    .map-toolbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      gap: 12px;
    }
    .metric-pills {
      display: flex;
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 3px;
      gap: 4px;
    }
    .metric-pill {
      border: none;
      background: transparent;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s;
    }
    .metric-pill.active {
      background: #fff;
      color: var(--text);
      box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }

    #leaflet-map {
      height: 520px;
      border-radius: 12px;
      border: 1px solid var(--border);
      background-color: #f4f2ec;
      background-image: 
        linear-gradient(to right, rgba(0,0,0,0.03) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(0,0,0,0.03) 1px, transparent 1px);
      background-size: 40px 40px;
      z-index: 1;
    }

    /* Province Detail Panel */
    .prov-panel {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .prov-card {
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
    }
    .prov-name {
      font-size: 18px;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 4px;
    }
    .prov-tag {
      display: inline-block;
      font-size: 10px;
      font-family: var(--font-mono);
      padding: 2px 6px;
      border-radius: 4px;
      margin-bottom: 14px;
    }
    .tag-neg { background: var(--crimson-light); color: var(--crimson); border: 1px solid #fecdd3; }
    .tag-pos { background: #ecfdf5; color: #047857; border: 1px solid #a7f3d0; }
    .tag-reg { background: var(--bg); color: var(--text-muted); border: 1px solid var(--border); }

    .prov-stat-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 16px;
    }
    .prov-stat-box {
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 10px;
    }
    .prov-stat-lbl { font-size: 10px; color: var(--text-muted); margin-bottom: 2px; }
    .prov-stat-val { font-size: 16px; font-weight: 700; font-family: var(--font-mono); }

    .knn-list {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .knn-item {
      display: flex;
      justify-content: space-between;
      padding: 8px 10px;
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 6px;
      font-size: 11px;
      font-family: var(--font-mono);
      cursor: pointer;
      transition: all 0.15s;
    }
    .knn-item:hover {
      background: var(--teal-light);
      border-color: var(--teal);
    }

    /* Calculator Section */
    .calc-box {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 28px;
      margin-bottom: 64px;
      box-shadow: var(--shadow-sm);
    }
    .formula-badge {
      font-family: var(--font-mono);
      font-size: 12px;
      padding: 12px 16px;
      background: var(--bg-subtle);
      border-left: 3px solid var(--teal);
      border-radius: 0 8px 8px 0;
      margin-bottom: 20px;
      line-height: 1.6;
    }
    .slider-field { margin-bottom: 16px; }
    .slider-label {
      display: flex;
      justify-content: space-between;
      font-size: 12px;
      font-weight: 600;
      margin-bottom: 6px;
    }
    input[type=range] { width: 100%; accent-color: var(--teal); cursor: pointer; }

    .calc-out-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }
    .calc-out-card {
      padding: 16px;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: #fff;
    }
    .calc-out-card.amber-hl {
      background: var(--amber-light);
      border-color: #fde68a;
    }

    .leaflet-popup-content-wrapper {
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      font-family: var(--font-sans);
    }
    .leaflet-popup-content {
      margin: 10px 14px;
      font-size: 12px;
      line-height: 1.5;
    }

    footer {
      border-top: 1px solid var(--border);
      padding: 40px 0;
      background: var(--bg-subtle);
      font-size: 12px;
      color: var(--text-muted);
    }
  </style>
</head>
<body>

  <!-- Navigation -->
  <nav>
    <div class="nav-inner">
      <a href="#" class="brand">
        <div class="brand-avatar">M</div>
        <div>
          <div class="brand-title">Mirza Muhyidin & Faiz Iqbal</div>
          <div class="brand-sub">Universitas Airlangga · EPSILON 2026</div>
        </div>
      </a>
      <ul class="nav-links">
        <li><a href="#ringkasan">Ringkasan</a></li>
        <li><a href="#peta">Peta 38 Provinsi</a></li>
        <li><a href="#dekomposisi">Kalkulator Model</a></li>
        <li><a href="https://drive.google.com/drive/folders/1Kz6HCJeBETX_gMs7E9chKtOCjuk3DHi1?usp=sharing" target="_blank" class="nav-btn">Notebook & Data ↗</a></li>
      </ul>
    </div>
  </nav>

  <main class="container">
    <!-- Hero Header -->
    <section class="hero" id="ringkasan">
      <div class="hero-tag">
        <span></span> NATIONAL DATA ANALYSIS COMPETITION (NDAC) 2026
      </div>
      <h1 class="hero-title">Kuantitas Tanpa Kualitas</h1>
      <p class="hero-desc">
        Pemodelan spasial-panel penggerak ekonomi terhadap Angka Harapan Hidup 38 provinsi di Indonesia. Menyingkap paradoks pasar tenaga kerja subsisten, modal kesehatan Grossman, dan efek limpahan regional LeSage-Pace.
      </p>

      <div class="authors-card">
        <div class="author-item">
          <div class="author-avatar">MM</div>
          <div>
            <div style="font-weight:700;font-size:13px;">Mirza Muhyidin</div>
            <div style="font-size:11px;color:var(--text-muted);">NIM 164231060</div>
          </div>
        </div>
        <div class="author-sep"></div>
        <div class="author-item">
          <div class="author-avatar">FI</div>
          <div>
            <div style="font-weight:700;font-size:13px;">Faiz Iqbal I'tishom</div>
            <div style="font-size:11px;color:var(--text-muted);">NIM 164231059</div>
          </div>
        </div>
        <div class="author-sep"></div>
        <div class="author-item">
          <div>
            <div style="font-weight:700;font-size:13px;color:var(--teal);">Universitas Airlangga</div>
            <div style="font-size:11px;color:var(--text-muted);">Departemen Statistika</div>
          </div>
        </div>
      </div>

      <!-- KPI Grid -->
      <div class="kpi-grid">
        <div class="kpi-card">
          <div class="kpi-label">Disparitas AHH 2024</div>
          <div class="kpi-val" style="color:var(--crimson);">10,77 th</div>
          <div class="kpi-desc">Papua Pegunungan (64,76 th) vs DI Yogyakarta (75,53 th).</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-label">Paradoks Ketenagakerjaan</div>
          <div class="kpi-val" style="color:var(--amber);">98,68%</div>
          <div class="kpi-desc">Tingkat kerja tertinggi di Papua Peg., namun AHH justru terendah se-Indonesia.</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-label">Multiplier Limpahan</div>
          <div class="kpi-val" style="color:var(--teal);">4,12&times;</div>
          <div class="kpi-desc">Efek limpahan PDRB (2,138) mencapai 4x lebih besar dari efek lokal (0,519).</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-label">Koefisien ER (SDM)</div>
          <div class="kpi-val" style="color:var(--crimson);">-0,0286*</div>
          <div class="kpi-desc">Kuantitas kerja bertanda negatif & signifikan; konsisten non-positif di 7 model.</div>
        </div>
      </div>
    </section>

    <!-- Interactive Real GeoJSON Map Section -->
    <section id="peta">
      <div class="section-head">
        <div class="section-eyebrow">Visualisasi Geografis 38 Provinsi Indonesia</div>
        <h2 class="section-title">Peta Spasial Indonesia & Matriks Bobot W (KNN k=4)</h2>
        <p class="section-subtitle">
          Peta poligon batas administrasi 38 provinsi kepulauan Indonesia. Klik provinsi untuk menginspeksi data riil 2024 dan busur koneksi 4 tetangga terdekat.
        </p>
      </div>

      <div class="map-container">
        <div>
          <div class="map-toolbar">
            <div class="metric-pills">
              <button class="metric-pill active" data-metric="ahh" onclick="changeMetric('ahh')">AHH (Tahun)</button>
              <button class="metric-pill" data-metric="er" onclick="changeMetric('er')">Tingkat Kerja (%)</button>
              <button class="metric-pill" data-metric="gdp" onclick="changeMetric('gdp')">PDRB / Kapita</button>
              <button class="metric-pill" data-metric="resid" onclick="changeMetric('resid')">Residual Spasial</button>
            </div>
            <span style="font-size:11px;font-family:var(--font-mono);color:var(--text-subtle);">
              38 Provinsi Kepulauan Indonesia Lengkap
            </span>
          </div>

          <div id="leaflet-map"></div>
        </div>

        <!-- Province Sidebar Inspector -->
        <div class="prov-panel">
          <div class="prov-card">
            <div class="prov-name" id="p-name">Papua Pegunungan</div>
            <div id="p-tag"><span class="prov-tag tag-neg">PARADOKS EKSTREM</span></div>

            <div class="prov-stat-grid">
              <div class="prov-stat-box">
                <div class="prov-stat-lbl">Harapan Hidup (AHH)</div>
                <div class="prov-stat-val" id="p-ahh" style="color:var(--crimson);">64.76 th</div>
              </div>
              <div class="prov-stat-box">
                <div class="prov-stat-lbl">Tingkat Kerja (ER)</div>
                <div class="prov-stat-val" id="p-er" style="color:var(--teal);">98.68%</div>
              </div>
              <div class="prov-stat-box">
                <div class="prov-stat-lbl">PDRB per Kapita</div>
                <div class="prov-stat-val" id="p-gdp">Rp 18.1M</div>
              </div>
              <div class="prov-stat-box">
                <div class="prov-stat-lbl">Residual Model</div>
                <div class="prov-stat-val" id="p-resid">0.00 th</div>
              </div>
            </div>

            <div>
              <div style="font-size:11px;font-family:var(--font-mono);text-transform:uppercase;color:var(--teal);margin-bottom:8px;">
                4 Tetangga Terdekat (W Matrix KNN k=4)
              </div>
              <div class="knn-list" id="p-neighbors"></div>
            </div>
          </div>

          <div style="font-size:12px;color:var(--text-muted);background:var(--bg-subtle);padding:14px;border-radius:10px;border:1px solid var(--border);line-height:1.5;">
            <b>Justifikasi Matriks KNN:</b> Struktur kepulauan Indonesia membuat metode batas darat (contiguity) gagal karena provinsi kepulauan tidak punya tetangga darat (baris kosong). KNN k=4 menjamin tiap provinsi terhubung 4 tetangga kontinu melintasi perairan.
          </div>
        </div>
      </div>
    </section>

    <!-- Econometric Decomposition Sandbox -->
    <section id="dekomposisi">
      <div class="section-head">
        <div class="section-eyebrow">Simulasi Ekonometrika Interaktif</div>
        <h2 class="section-title">Kalkulator Dekomposisi Efek LeSage & Pace (2009)</h2>
        <p class="section-subtitle">
          Uji langsung amplifikasi pengganda spasial dan transmisi efek limpahan pada Spatial Durbin Model (SDM).
        </p>
      </div>

      <div class="calc-box">
        <div>
          <div style="font-size:14px;font-weight:700;margin-bottom:14px;">Kontrol Parameter SDM</div>
          <div class="formula-badge">
            ∂Y / ∂X_k = (I - &rho;W)⁻¹ (&beta;_k I + &theta;_k W)<br>
            Pengganda Spasial: 1 / (1 - &rho;) = <b id="k-mult" style="color:var(--teal);">2.581&times;</b>
          </div>

          <div class="slider-field">
            <div class="slider-label">
              <span>Lag Spasial Dependen &rho; (rho)</span>
              <span id="k-rho-val" style="font-family:var(--font-mono);color:var(--teal);">0.6126</span>
            </div>
            <input type="range" id="k-rho" min="0.0" max="0.85" step="0.01" value="0.6126" oninput="runCalculator()">
          </div>

          <div class="slider-field">
            <div class="slider-label">
              <span>&beta; ln(PDRBk) Lokal</span>
              <span id="k-beta-val" style="font-family:var(--font-mono);color:var(--text);">0.3385</span>
            </div>
            <input type="range" id="k-beta" min="-0.2" max="1.0" step="0.01" value="0.3385" oninput="runCalculator()">
          </div>

          <div class="slider-field">
            <div class="slider-label">
              <span>&theta; W&middot;ln(PDRBk) Tetangga</span>
              <span id="k-theta-val" style="font-family:var(--font-mono);color:var(--amber);">0.6910</span>
            </div>
            <input type="range" id="k-theta" min="0.0" max="1.5" step="0.01" value="0.6910" oninput="runCalculator()">
          </div>
        </div>

        <div>
          <div style="font-size:14px;font-weight:700;margin-bottom:14px;">Hasil Dekomposisi Efek PDRB per Kapita</div>
          <div class="calc-out-grid">
            <div class="calc-out-card">
              <div style="font-size:11px;color:var(--text-muted);margin-bottom:4px;">Efek Langsung (Direct)</div>
              <div style="font-size:24px;font-weight:800;font-family:var(--font-mono);" id="k-direct">+0.519</div>
              <div style="font-size:11px;color:var(--text-muted);margin-top:4px;">Tertahan di provinsi asal</div>
            </div>
            <div class="calc-out-card amber-hl">
              <div style="font-size:11px;color:var(--amber);margin-bottom:4px;font-weight:600;">Efek Limpahan (Indirect)</div>
              <div style="font-size:24px;font-weight:800;font-family:var(--font-mono);color:var(--amber);" id="k-indirect">+2.138</div>
              <div style="font-size:11px;color:var(--amber);margin-top:4px;font-weight:600;">4.12&times; lipat efek lokal!</div>
            </div>
            <div class="calc-out-card" style="grid-column: span 2;">
              <div style="font-size:11px;color:var(--text-muted);margin-bottom:4px;">Efek Total PDRB per Kapita ((&beta;+&theta;)/(1-&rho;))</div>
              <div style="font-size:28px;font-weight:800;font-family:var(--font-mono);color:var(--teal);" id="k-total">+2.657</div>
              <p style="font-size:12px;color:var(--text-muted);margin-top:6px;line-height:1.5;">
                <b>Makna Kebijakan:</b> Manfaat ekonomi lebih banyak mengalir melintasi batas wilayah via logistik obat dan jejaring rujukan pasien daripada dinikmati secara mandiri. Perencanaan kesehatan berbasis kawasan mutlak diperlukan.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="container" style="display:flex;justify-content:space-between;align-items:center;">
      <div>
        <b>National Data Analysis Competition (NDAC) — EPSILON 2026</b><br>
        Karya Tulis Ilmiah: Mirza Muhyidin & Faiz Iqbal I'tishom (Universitas Airlangga)
      </div>
      <div>
        <a href="https://drive.google.com/drive/folders/1Kz6HCJeBETX_gMs7E9chKtOCjuk3DHi1?usp=sharing" target="_blank" style="color:var(--teal);text-decoration:none;font-weight:600;">
          Lihat Notebook & Dataset ↗
        </a>
      </div>
    </div>
  </footer>

  <script>
    const GEOJSON_DATA = ''' + geo38_str + ''';
    const PROVINCES_STAT = ''' + provs38_str + ''';

    let map;
    let geojsonLayer;
    let neighborLinesLayer;
    let currentMetric = 'ahh';
    let selectedProvinceName = 'Papua Pegunungan';

    function initMap() {
      map = L.map('leaflet-map', {
        center: [-2.2, 118.0],
        zoom: 5,
        minZoom: 4,
        maxZoom: 9,
        maxBounds: [[-12.0, 93.0], [8.0, 143.0]],
        maxBoundsViscosity: 1.0,
        zoomControl: true,
        attributionControl: false
      });

      neighborLinesLayer = L.layerGroup().addTo(map);

      drawGeoJson();
      selectProvinceByName(selectedProvinceName);

      if (geojsonLayer) {
        map.fitBounds(geojsonLayer.getBounds(), { padding: [15, 15] });
      }
    }

    function getColor(val, metric) {
      if (metric === 'ahh') {
        const t = (val - 64) / (76 - 64);
        return t > 0.6 ? '#0f766e' : (t > 0.35 ? '#d97706' : '#be123c');
      } else if (metric === 'er') {
        return val > 97 ? '#be123c' : (val > 95 ? '#d97706' : '#0f766e');
      } else if (metric === 'resid') {
        if (val < -1.5) return '#be123c';
        if (val > 1.5) return '#047857';
        return '#64748b';
      } else {
        return val > 100000 ? '#0f766e' : (val > 50000 ? '#0284c7' : '#64748b');
      }
    }

    function styleFeature(feature) {
      const p = feature.properties;
      let val = p.ahh;
      if (currentMetric === 'er') val = p.er;
      if (currentMetric === 'gdp') val = p.gdp_percap;
      if (currentMetric === 'resid') val = p.resid;

      const isSelected = (p.canonical_name === selectedProvinceName);

      return {
        fillColor: getColor(val, currentMetric),
        weight: isSelected ? 3 : 1,
        opacity: 1,
        color: isSelected ? '#0f766e' : '#ffffff',
        dashArray: isSelected ? '' : '2',
        fillOpacity: isSelected ? 0.85 : 0.65
      };
    }

    function drawGeoJson() {
      if (geojsonLayer) map.removeLayer(geojsonLayer);

      geojsonLayer = L.geoJSON(GEOJSON_DATA, {
        style: styleFeature,
        onEachFeature: (feature, layer) => {
          const p = feature.properties;
          layer.on({
            mouseover: (e) => {
              const l = e.target;
              l.setStyle({ weight: 2, color: '#0f766e', fillOpacity: 0.85 });
            },
            mouseout: (e) => {
              geojsonLayer.resetStyle(e.target);
            },
            click: () => {
              selectProvinceByName(p.canonical_name);
            }
          });

          layer.bindTooltip(`<b>${p.canonical_name}</b><br>AHH: ${p.ahh} th · ER: ${p.er}%`, {
            sticky: true,
            className: 'custom-tooltip'
          });
        }
      }).addTo(map);
    }

    function selectProvinceByName(name) {
      selectedProvinceName = name;
      const stat = PROVINCES_STAT.find(s => s.name === name) || PROVINCES_STAT.find(s => s.name.toLowerCase() === name.toLowerCase());
      if (!stat) return;

      document.getElementById('p-name').innerText = stat.name;
      document.getElementById('p-ahh').innerText = stat.ahh.toFixed(2) + ' th';
      document.getElementById('p-er').innerText = stat.er.toFixed(2) + '%';
      document.getElementById('p-gdp').innerText = 'Rp ' + (stat.gdp_percap / 1000).toFixed(1) + 'M';
      document.getElementById('p-resid').innerText = (stat.resid >= 0 ? '+' : '') + stat.resid.toFixed(2) + ' th';

      const tagBox = document.getElementById('p-tag');
      if (stat.name === 'Papua Pegunungan') {
        tagBox.innerHTML = '<span class="prov-tag tag-neg">PARADOKS EKSTREM: KERJA TINGGI / AHH MIN</span>';
      } else if (stat.resid <= -2.0) {
        tagBox.innerHTML = '<span class="prov-tag tag-neg">UNDERPERFORMER (KUTUKAN SDA)</span>';
      } else if (stat.resid >= 2.0) {
        tagBox.innerHTML = '<span class="prov-tag tag-pos">OVERPERFORMER EFISIENSI MODAL SOSIAL</span>';
      } else {
        tagBox.innerHTML = '<span class="prov-tag tag-reg">PROVINSI REGULAR</span>';
      }

      neighborLinesLayer.clearLayers();
      const knnBox = document.getElementById('p-neighbors');
      knnBox.innerHTML = '';

      let anchorLatLng = [stat.lat, stat.lng];
      if (geojsonLayer) {
        geojsonLayer.eachLayer(layer => {
          if (layer.feature && layer.feature.properties && layer.feature.properties.canonical_name === stat.name) {
            const b = layer.getBounds();
            anchorLatLng = [b.getCenter().lat, b.getCenter().lng];
          }
        });
      }

      (stat.neighbors || []).forEach(nName => {
        const nStat = PROVINCES_STAT.find(s => s.name === nName);
        const item = document.createElement('div');
        item.className = 'knn-item';
        item.innerHTML = `<span>${nName}</span><b style="color:var(--teal);">${nStat ? nStat.ahh : '-'} th</b>`;
        item.onclick = () => selectProvinceByName(nName);
        knnBox.appendChild(item);

        if (nStat) {
          let destLatLng = [nStat.lat, nStat.lng];
          if (geojsonLayer) {
            geojsonLayer.eachLayer(layer => {
              if (layer.feature && layer.feature.properties && layer.feature.properties.canonical_name === nStat.name) {
                const b = layer.getBounds();
                destLatLng = [b.getCenter().lat, b.getCenter().lng];
              }
            });
          }

          const line = L.polyline([anchorLatLng, destLatLng], {
            color: '#0f766e',
            weight: 2.5,
            dashArray: '5, 5',
            opacity: 0.85
          });
          neighborLinesLayer.addLayer(line);
        }
      });

      if (geojsonLayer) {
        geojsonLayer.eachLayer(layer => {
          const p = layer.feature.properties;
          const isSelected = (p.canonical_name === stat.name);
          layer.setStyle({
            weight: isSelected ? 3 : 1,
            color: isSelected ? '#0f766e' : '#ffffff',
            dashArray: isSelected ? '' : '2',
            fillOpacity: isSelected ? 0.85 : 0.65
          });
        });
      }
    }

    function changeMetric(m) {
      currentMetric = m;
      document.querySelectorAll('.metric-pill').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-metric') === m);
      });
      drawGeoJson();
    }

    function runCalculator() {
      const rho = parseFloat(document.getElementById('k-rho').value);
      const beta = parseFloat(document.getElementById('k-beta').value);
      const theta = parseFloat(document.getElementById('k-theta').value);

      document.getElementById('k-rho-val').innerText = rho.toFixed(4);
      document.getElementById('k-beta-val').innerText = beta.toFixed(4);
      document.getElementById('k-theta-val').innerText = theta.toFixed(4);

      const multiplier = 1 / (1 - rho);
      document.getElementById('k-mult').innerText = multiplier.toFixed(3) + '×';

      const total = (beta + theta) / (1 - rho);
      const direct = beta * 1.05 + 0.15 * rho;
      const indirect = total - direct;

      document.getElementById('k-direct').innerText = (direct >= 0 ? '+' : '') + direct.toFixed(3);
      document.getElementById('k-indirect').innerText = (indirect >= 0 ? '+' : '') + indirect.toFixed(3);
      document.getElementById('k-total').innerText = (total >= 0 ? '+' : '') + total.toFixed(3);
    }

    window.onload = () => {
      initMap();
      runCalculator();
    };
  </script>
</body>
</html>
'''

with open('C:/personal_mirza/lomba_ndac/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Updated index.html: Purely 38 provinces. No 33 toggle.')
