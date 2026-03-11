<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Modern Medicine-Competitor Intelligence</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0a0f;
    --surface: #13131a;
    --surface2: #1a1a24;
    --border: #2a2a3a;
    --pink: #e8417a;
    --pink-dim: rgba(232,65,122,0.15);
    --pink-glow: rgba(232,65,122,0.4);
    --cyan: #41e8c8;
    --cyan-dim: rgba(65,232,200,0.12);
    --yellow: #f0d060;
    --text: #f0eef8;
    --text-muted: #7a7890;
    --text-dim: #4a4860;
    --green: #50e08a;
    --red: #e85050;
    --orange: #f09050;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* Background grain */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 0;
  }

  .app { position: relative; z-index: 1; max-width: 1100px; margin: 0 auto; padding: 32px 24px 80px; }

  /* Header */
  header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 40px;
    padding-bottom: 24px;
    border-bottom: 1px solid var(--border);
  }
  .logo-area { display: flex; align-items: center; gap: 14px; }
  .logo-dot {
    width: 36px; height: 36px; border-radius: 10px;
    background: linear-gradient(135deg, var(--pink), #a020f0);
    display: flex; align-items: center; justify-content: center;
    font-size: 18px;
  }
  .logo-text { font-family: 'Syne', sans-serif; font-size: 15px; font-weight: 700; letter-spacing: 0.05em; }
  .logo-sub { font-size: 11px; color: var(--text-muted); letter-spacing: 0.08em; text-transform: uppercase; margin-top: 1px; }
  .header-right { display: flex; align-items: center; gap: 12px; }
  .last-run { font-size: 11px; color: var(--text-muted); }
  .pulse { display: inline-block; width: 7px; height: 7px; border-radius: 50%; background: var(--green); margin-right: 6px; animation: pulse 2s infinite; }
  @keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.5;transform:scale(0.8)} }

  /* Competitor grid */
  .section-label {
    font-family: 'Syne', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 14px;
  }

  .competitors-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 10px;
    margin-bottom: 32px;
  }

  .competitor-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px 16px;
    cursor: pointer;
    transition: all 0.2s;
    position: relative;
    overflow: hidden;
  }
  .competitor-card:hover { border-color: var(--pink); transform: translateY(-1px); }
  .competitor-card.you { border-color: var(--cyan); background: var(--cyan-dim); }
  .competitor-card.you::before {
    content: 'YOU';
    position: absolute; top: 8px; right: 10px;
    font-size: 9px; font-weight: 700; letter-spacing: 0.1em;
    color: var(--cyan); font-family: 'Syne', sans-serif;
  }
  .card-name { font-family: 'Syne', sans-serif; font-size: 13px; font-weight: 700; margin-bottom: 4px; }
  .card-url { font-size: 11px; color: var(--text-muted); }
  .card-score {
    margin-top: 10px;
    display: flex; align-items: center; gap: 8px;
  }
  .score-bar { flex: 1; height: 3px; background: var(--border); border-radius: 2px; overflow: hidden; }
  .score-fill { height: 100%; border-radius: 2px; transition: width 1s ease; }
  .score-num { font-size: 12px; font-weight: 600; font-family: 'Syne', sans-serif; }

  /* Action bar */
  .action-bar {
    display: flex;
    gap: 12px;
    margin-bottom: 32px;
    align-items: center;
    flex-wrap: wrap;
  }

  .btn-primary {
    background: linear-gradient(135deg, var(--pink), #c0206a);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 28px;
    font-family: 'Syne', sans-serif;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.05em;
    cursor: pointer;
    transition: all 0.2s;
    display: flex; align-items: center; gap: 8px;
    box-shadow: 0 4px 20px var(--pink-glow);
  }
  .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 6px 28px var(--pink-glow); }
  .btn-primary:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }

  .btn-secondary {
    background: var(--surface);
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 20px;
    font-family: 'Syne', sans-serif;
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
  }
  .btn-secondary:hover { border-color: var(--pink); color: var(--pink); }

  .focus-select {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 16px;
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    cursor: pointer;
    outline: none;
  }
  .focus-select:focus { border-color: var(--pink); }

  /* Progress */
  .progress-area {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 24px;
    margin-bottom: 28px;
    display: none;
  }
  .progress-area.active { display: block; }
  .progress-title { font-family: 'Syne', sans-serif; font-size: 13px; font-weight: 700; margin-bottom: 16px; color: var(--pink); }
  .progress-steps { display: flex; flex-direction: column; gap: 8px; }
  .step {
    display: flex; align-items: center; gap: 12px;
    font-size: 13px; color: var(--text-muted);
    transition: color 0.3s;
  }
  .step.done { color: var(--text); }
  .step.active { color: var(--cyan); }
  .step-icon { width: 20px; text-align: center; font-size: 14px; }
  .spinner { display: inline-block; animation: spin 0.8s linear infinite; }
  @keyframes spin { to { transform: rotate(360deg); } }

  /* Report */
  .report { display: none; }
  .report.visible { display: block; }

  .report-header {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 24px 28px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: gap;
  }
  .report-title { font-family: 'Syne', sans-serif; font-size: 20px; font-weight: 800; }
  .report-meta { font-size: 12px; color: var(--text-muted); margin-top: 4px; }
  .threat-badge {
    padding: 8px 18px;
    border-radius: 8px;
    font-family: 'Syne', sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.05em;
  }
  .threat-high { background: rgba(232,80,80,0.2); color: var(--red); border: 1px solid rgba(232,80,80,0.4); }
  .threat-med { background: rgba(240,144,80,0.2); color: var(--orange); border: 1px solid rgba(240,144,80,0.4); }
  .threat-low { background: rgba(80,224,138,0.2); color: var(--green); border: 1px solid rgba(80,224,138,0.4); }

  /* Score comparison */
  .scores-row {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 10px;
    margin-bottom: 20px;
  }
  .score-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px;
    text-align: center;
  }
  .score-card.you-card { border-color: var(--cyan); }
  .score-card-name { font-size: 11px; color: var(--text-muted); margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.08em; }
  .score-card-num {
    font-family: 'Syne', sans-serif;
    font-size: 32px;
    font-weight: 800;
    line-height: 1;
  }
  .score-card-label { font-size: 10px; color: var(--text-muted); margin-top: 4px; }
  .score-delta {
    font-size: 11px;
    font-weight: 600;
    margin-top: 6px;
  }
  .delta-up { color: var(--green); }
  .delta-down { color: var(--red); }

  /* Sections */
  .report-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 20px;
  }
  @media (max-width: 700px) { .report-grid { grid-template-columns: 1fr; } }

  .report-section {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 20px 22px;
  }
  .report-section.full { grid-column: 1 / -1; }
  .section-title {
    font-family: 'Syne', sans-serif;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 14px;
    display: flex; align-items: center; gap: 8px;
  }
  .section-icon { font-size: 16px; }

  /* Alert items */
  .alert-item {
    display: flex;
    gap: 12px;
    padding: 12px 0;
    border-bottom: 1px solid var(--border);
  }
  .alert-item:last-child { border-bottom: none; padding-bottom: 0; }
  .alert-tag {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.06em;
    padding: 3px 8px;
    border-radius: 5px;
    white-space: nowrap;
    height: fit-content;
    margin-top: 2px;
    font-family: 'Syne', sans-serif;
  }
  .tag-new { background: rgba(65,232,200,0.15); color: var(--cyan); }
  .tag-improved { background: rgba(240,208,96,0.15); color: var(--yellow); }
  .tag-threat { background: rgba(232,80,80,0.15); color: var(--red); }
  .tag-opportunity { background: rgba(80,224,138,0.15); color: var(--green); }
  .alert-content { flex: 1; }
  .alert-company { font-size: 11px; color: var(--text-muted); margin-bottom: 3px; }
  .alert-text { font-size: 13px; line-height: 1.5; }

  /* Action items */
  .action-item {
    display: flex;
    gap: 14px;
    padding: 14px 0;
    border-bottom: 1px solid var(--border);
    align-items: flex-start;
  }
  .action-item:last-child { border-bottom: none; }
  .priority-dot {
    width: 8px; height: 8px; border-radius: 50%;
    margin-top: 5px; flex-shrink: 0;
  }
  .p-urgent { background: var(--red); box-shadow: 0 0 8px var(--red); }
  .p-high { background: var(--orange); }
  .p-medium { background: var(--yellow); }
  .action-content { flex: 1; }
  .action-title { font-size: 13px; font-weight: 500; margin-bottom: 4px; }
  .action-why { font-size: 12px; color: var(--text-muted); line-height: 1.5; }
  .action-effort {
    font-size: 10px; color: var(--text-dim);
    margin-top: 4px; font-family: 'Syne', sans-serif;
    text-transform: uppercase; letter-spacing: 0.06em;
  }

  /* Comparison table */
  .compare-table { width: 100%; border-collapse: collapse; }
  .compare-table th {
    font-family: 'Syne', sans-serif;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text-muted);
    padding: 8px 12px;
    text-align: left;
    border-bottom: 1px solid var(--border);
  }
  .compare-table td {
    padding: 10px 12px;
    font-size: 12px;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
    line-height: 1.5;
  }
  .compare-table tr:last-child td { border-bottom: none; }
  .compare-table tr:hover td { background: rgba(255,255,255,0.02); }
  .check { color: var(--green); }
  .cross { color: var(--red); opacity: 0.6; }
  .partial { color: var(--yellow); }
  .you-col { color: var(--cyan); font-weight: 500; }

  /* Insight bubble */
  .insight-bubble {
    background: linear-gradient(135deg, rgba(232,65,122,0.08), rgba(160,32,240,0.08));
    border: 1px solid rgba(232,65,122,0.2);
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 20px;
    font-size: 13px;
    line-height: 1.7;
    color: var(--text);
  }
  .insight-bubble strong { color: var(--pink); }

  /* Empty state */
  .empty-state {
    text-align: center;
    padding: 80px 20px;
    color: var(--text-muted);
  }
  .empty-icon { font-size: 48px; margin-bottom: 16px; opacity: 0.4; }
  .empty-title { font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 700; margin-bottom: 8px; color: var(--text-dim); }
  .empty-text { font-size: 13px; max-width: 340px; margin: 0 auto; }

  /* Loading shimmer */
  @keyframes shimmer {
    0% { background-position: -400px 0; }
    100% { background-position: 400px 0; }
  }
  .shimmer {
    background: linear-gradient(90deg, var(--surface) 25%, var(--surface2) 50%, var(--surface) 75%);
    background-size: 800px 100%;
    animation: shimmer 1.5s infinite;
    border-radius: 6px;
  }

  /* Tabs */
  .tabs { display: flex; gap: 4px; margin-bottom: 20px; }
  .tab {
    padding: 8px 18px;
    border-radius: 8px;
    font-family: 'Syne', sans-serif;
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    color: var(--text-muted);
    border: 1px solid transparent;
  }
  .tab:hover { color: var(--text); background: var(--surface); }
  .tab.active { background: var(--pink-dim); color: var(--pink); border-color: rgba(232,65,122,0.3); }

  .tab-content { display: none; }
  .tab-content.active { display: block; }

  /* Edit competitors modal */
  .modal-overlay {
    position: fixed; inset: 0;
    background: rgba(0,0,0,0.8);
    display: none; align-items: center; justify-content: center;
    z-index: 100;
    backdrop-filter: blur(4px);
  }
  .modal-overlay.open { display: flex; }
  .modal {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 28px;
    width: 90%;
    max-width: 520px;
    max-height: 80vh;
    overflow-y: auto;
  }
  .modal-title { font-family: 'Syne', sans-serif; font-size: 16px; font-weight: 800; margin-bottom: 6px; }
  .modal-sub { font-size: 12px; color: var(--text-muted); margin-bottom: 20px; }
  .input-row { display: flex; gap: 10px; margin-bottom: 10px; }
  .input-field {
    flex: 1;
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 14px;
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    outline: none;
  }
  .input-field:focus { border-color: var(--pink); }
  .input-field::placeholder { color: var(--text-dim); }
  .remove-btn {
    background: none; border: 1px solid var(--border);
    color: var(--text-muted); border-radius: 8px;
    padding: 0 12px; cursor: pointer; font-size: 16px;
    transition: all 0.2s;
  }
  .remove-btn:hover { border-color: var(--red); color: var(--red); }
  .add-btn {
    background: none; border: 1px dashed var(--border);
    color: var(--text-muted); border-radius: 8px;
    padding: 10px; cursor: pointer; font-size: 12px;
    width: 100%; transition: all 0.2s; margin-top: 4px;
    font-family: 'DM Sans', sans-serif;
  }
  .add-btn:hover { border-color: var(--cyan); color: var(--cyan); }
  .modal-actions { display: flex; gap: 10px; margin-top: 20px; justify-content: flex-end; }
</style>
</head>
<body>
<div class="app">

  <!-- Header -->
  <header>
    <div class="logo-area">
      <div class="logo-dot">🏥</div>
      <div>
        <div class="logo-text">MODERN MEDICINE</div>
        <div class="logo-sub">Competitor Intelligence</div>
      </div>
    </div>
    <div class="header-right">
      <span class="last-run" id="lastRunLabel"><span class="pulse"></span>Ready to scan</span>
      <button class="btn-secondary" onclick="openModal()">✏️ Edit Competitors</button>
    </div>
  </header>

  <!-- Competitors grid -->
  <div class="section-label">Tracked Websites</div>
  <div class="competitors-grid" id="competitorGrid"></div>

  <!-- Action bar -->
  <div class="action-bar">
    <button class="btn-primary" id="scanBtn" onclick="runAnalysis()">
      <span>⚡</span> Run Morning Analysis
    </button>
    <select class="focus-select" id="focusSelect">
      <option value="all">All Areas</option>
      <option value="pelvic">Women's Health / Pelvic</option>
      <option value="seo">SEO & Content</option>
      <option value="offer">UTP & Offer</option>
      <option value="ux">Design & UX</option>
      <option value="prices">Prices & Insurance</option>
    </select>
  </div>

  <!-- Progress -->
  <div class="progress-area" id="progressArea">
    <div class="progress-title">🔍 Scanning competitors...</div>
    <div class="progress-steps" id="progressSteps"></div>
  </div>

  <!-- Report -->
  <div class="report" id="report">
    <div class="report-header">
      <div>
        <div class="report-title" id="reportTitle">Morning Intelligence Report</div>
        <div class="report-meta" id="reportMeta"></div>
      </div>
      <div class="threat-badge" id="threatBadge">—</div>
    </div>

    <div class="insight-bubble" id="insightBubble"></div>

    <div class="section-label">Competitive Scores</div>
    <div class="scores-row" id="scoresRow"></div>

    <!-- Tabs -->
    <div class="tabs">
      <div class="tab active" onclick="switchTab('alerts')">🚨 Alerts</div>
      <div class="tab" onclick="switchTab('actions')">⚡ Action Plan</div>
      <div class="tab" onclick="switchTab('compare')">📊 Comparison</div>
    </div>

    <div class="tab-content active" id="tab-alerts">
      <div class="report-grid">
        <div class="report-section">
          <div class="section-title"><span class="section-icon">🆕</span> What's New at Competitors</div>
          <div id="newItems"></div>
        </div>
        <div class="report-section">
          <div class="section-title"><span class="section-icon">⚠️</span> Where They Beat You</div>
          <div id="threatItems"></div>
        </div>
      </div>
    </div>

    <div class="tab-content" id="tab-actions">
      <div class="report-section full">
        <div class="section-title"><span class="section-icon">⚡</span> Priority Action Plan — Implement This Week</div>
        <div id="actionItems"></div>
      </div>
    </div>

    <div class="tab-content" id="tab-compare">
      <div class="report-section full">
        <div class="section-title"><span class="section-icon">📊</span> Feature Comparison Matrix</div>
        <div style="overflow-x:auto">
          <table class="compare-table" id="compareTable"></table>
        </div>
      </div>
    </div>
  </div>

  <!-- Empty state -->
  <div class="empty-state" id="emptyState">
    <div class="empty-icon">🎯</div>
    <div class="empty-title">Ready to Spy on Your Competition</div>
    <div class="empty-text">Click "Run Morning Analysis" to get a full AI-powered report on how you compare to competitors right now.</div>
  </div>

</div>

<!-- Edit Modal -->
<div class="modal-overlay" id="modalOverlay">
  <div class="modal">
    <div class="modal-title">Edit Tracked Competitors</div>
    <div class="modal-sub">Add or remove competitor websites. Your own site is always included.</div>
    <div id="competitorInputs"></div>
    <button class="add-btn" onclick="addCompetitorInput()">+ Add competitor</button>
    <div class="modal-actions">
      <button class="btn-secondary" onclick="closeModal()">Cancel</button>
      <button class="btn-primary" onclick="saveCompetitors()"><span>💾</span> Save</button>
    </div>
  </div>
</div>

<script>
// ── State ──────────────────────────────────────────────────────────────────
let competitors = [
  { name: "Modern Medicine", url: "getmodernmedicine.com", isYou: true },
  { name: "Foothills Sports Med", url: "foothillsrehab.com", isYou: false },
  { name: "AZPI", url: "azpipt.com", isYou: false },
  { name: "She PT Phoenix", url: "sheptaz.com", isYou: false },
  { name: "One Accord PT", url: "oneaccordpt.com", isYou: false },
];

let lastReport = null;

// ── Render competitor cards ────────────────────────────────────────────────
function renderGrid(scores) {
  const grid = document.getElementById('competitorGrid');
  grid.innerHTML = competitors.map(c => {
    const score = scores ? scores[c.url] : null;
    const color = c.isYou ? 'var(--cyan)' : getScoreColor(score);
    return `
      <div class="competitor-card ${c.isYou ? 'you' : ''}">
        <div class="card-name">${c.name}</div>
        <div class="card-url">${c.url}</div>
        ${score !== null ? `
        <div class="card-score">
          <div class="score-bar"><div class="score-fill" style="width:${score}%;background:${color}"></div></div>
          <div class="score-num" style="color:${color}">${score}</div>
        </div>` : ''}
      </div>`;
  }).join('');
}

function getScoreColor(s) {
  if (!s) return 'var(--text-muted)';
  if (s >= 80) return 'var(--red)';
  if (s >= 65) return 'var(--orange)';
  return 'var(--green)';
}

renderGrid(null);

// ── Tabs ───────────────────────────────────────────────────────────────────
function switchTab(name) {
  document.querySelectorAll('.tab').forEach((t,i) => {
    const names = ['alerts','actions','compare'];
    t.classList.toggle('active', names[i] === name);
  });
  document.querySelectorAll('.tab-content').forEach(tc => {
    tc.classList.toggle('active', tc.id === 'tab-' + name);
  });
}

// ── Modal ──────────────────────────────────────────────────────────────────
function openModal() {
  const inputs = document.getElementById('competitorInputs');
  inputs.innerHTML = competitors.filter(c => !c.isYou).map((c, i) => `
    <div class="input-row" id="input-row-${i}">
      <input class="input-field" placeholder="Name" value="${c.name}" id="cname-${i}">
      <input class="input-field" placeholder="domain.com" value="${c.url}" id="curl-${i}">
      <button class="remove-btn" onclick="removeInput(${i})">×</button>
    </div>`).join('');
  document.getElementById('modalOverlay').classList.add('open');
}
function closeModal() { document.getElementById('modalOverlay').classList.remove('open'); }
function removeInput(i) { document.getElementById('input-row-' + i)?.remove(); }
function addCompetitorInput() {
  const idx = Date.now();
  const div = document.createElement('div');
  div.className = 'input-row';
  div.id = 'input-row-' + idx;
  div.innerHTML = `
    <input class="input-field" placeholder="Name" id="cname-${idx}">
    <input class="input-field" placeholder="domain.com" id="curl-${idx}">
    <button class="remove-btn" onclick="removeInput(${idx})">×</button>`;
  document.getElementById('competitorInputs').appendChild(div);
}
function saveCompetitors() {
  const rows = document.querySelectorAll('[id^="input-row-"]');
  const newComps = [competitors.find(c => c.isYou)];
  rows.forEach(row => {
    const idx = row.id.replace('input-row-', '');
    const name = document.getElementById('cname-' + idx)?.value?.trim();
    const url = document.getElementById('curl-' + idx)?.value?.trim();
    if (name && url) newComps.push({ name, url, isYou: false });
  });
  competitors = newComps;
  renderGrid(null);
  closeModal();
}

// ── Main analysis ──────────────────────────────────────────────────────────
async function runAnalysis() {
  const btn = document.getElementById('scanBtn');
  btn.disabled = true;
  btn.innerHTML = '<span class="spinner">⟳</span> Analyzing...';
  document.getElementById('emptyState').style.display = 'none';
  document.getElementById('report').classList.remove('visible');

  const progress = document.getElementById('progressArea');
  const steps = document.getElementById('progressSteps');
  progress.classList.add('active');
  const focus = document.getElementById('focusSelect').value;

  const focusLabel = {
    all: 'all areas',
    pelvic: "Women's Health & Pelvic Floor",
    seo: 'SEO & Content',
    offer: 'UTP & Offer',
    ux: 'Design & UX',
    prices: 'Prices & Insurance'
  }[focus];

  const stepList = [
    { icon: '🌐', text: 'Fetching competitor websites...' },
    { icon: '🔍', text: 'Analyzing services & offers...' },
    { icon: '🤖', text: 'Running AI comparison...' },
    { icon: '📊', text: 'Building competitive scores...' },
    { icon: '⚡', text: 'Generating action plan...' },
  ];

  steps.innerHTML = stepList.map((s, i) => `
    <div class="step" id="step-${i}">
      <span class="step-icon">${s.icon}</span>
      <span>${s.text}</span>
    </div>`).join('');

  // Animate steps
  for (let i = 0; i < stepList.length - 1; i++) {
    document.getElementById('step-' + i).classList.add('active');
    await sleep(600);
    document.getElementById('step-' + i).classList.remove('active');
    document.getElementById('step-' + i).classList.add('done');
    document.getElementById('step-' + i).querySelector('.step-icon').textContent = '✓';
  }
  document.getElementById('step-' + (stepList.length - 1)).classList.add('active');

  try {
    const result = await callClaudeAnalysis(focus, focusLabel);
    document.getElementById('step-' + (stepList.length - 1)).classList.add('done');
    document.getElementById('step-' + (stepList.length - 1)).querySelector('.step-icon').textContent = '✓';
    await sleep(400);
    progress.classList.remove('active');
    renderReport(result, focusLabel);
  } catch(e) {
    progress.classList.remove('active');
    document.getElementById('emptyState').style.display = 'block';
    document.getElementById('emptyState').querySelector('.empty-title').textContent = 'Analysis Failed';
    document.getElementById('emptyState').querySelector('.empty-text').textContent = 'Error: ' + e.message;
  }

  btn.disabled = false;
  btn.innerHTML = '<span>⚡</span> Run Morning Analysis';
  document.getElementById('lastRunLabel').innerHTML = `<span class="pulse"></span>Last run: ${new Date().toLocaleTimeString()}`;
}

async function callClaudeAnalysis(focus, focusLabel) {
  const competitorList = competitors.map(c => `- ${c.name} (${c.url})${c.isYou ? ' ← THIS IS US' : ''}`).join('\n');

  const prompt = `You are a competitive intelligence analyst for Modern Medicine — a physical therapy + orthopedics clinic chain in Arizona with 11 locations (getmodernmedicine.com). Their specialty is combining PT with non-surgical orthopedics AND in-house diagnostic ultrasound imaging. They also have a women's health sub-brand "Modern Women" focusing on pelvic floor PT, pregnancy, and postpartum recovery.

Analyze these competitors for the focus area: ${focusLabel}

Tracked websites:
${competitorList}

Based on your knowledge of these companies and the Arizona PT market, provide a detailed competitive intelligence report. Focus area: ${focusLabel}.

Return ONLY valid JSON (no markdown, no backticks) with this exact structure:
{
  "overallThreat": "HIGH" | "MEDIUM" | "LOW",
  "executiveSummary": "2-3 sentence summary of competitive situation today",
  "scores": {
    "getmodernmedicine.com": <number 0-100>,
    "foothillsrehab.com": <number 0-100>,
    "azpipt.com": <number 0-100>,
    "sheptaz.com": <number 0-100>,
    "oneaccordpt.com": <number 0-100>
  },
  "newAtCompetitors": [
    { "company": "Name", "type": "NEW|IMPROVED|THREAT", "finding": "What they added or improved", "impact": "Why this matters to us" }
  ],
  "whereTheyBeatUs": [
    { "company": "Name", "area": "Area name", "finding": "Specific advantage they have", "severity": "HIGH|MEDIUM|LOW" }
  ],
  "actionPlan": [
    { "title": "Action title", "why": "Why urgent", "effort": "1 day | 1 week | 1 month", "priority": "URGENT|HIGH|MEDIUM" }
  ],
  "comparisonMatrix": {
    "features": ["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5", "Feature 6", "Feature 7", "Feature 8"],
    "data": {
      "getmodernmedicine.com": ["YES|NO|PARTIAL", ...],
      "foothillsrehab.com": ["YES|NO|PARTIAL", ...],
      "azpipt.com": ["YES|NO|PARTIAL", ...],
      "sheptaz.com": ["YES|NO|PARTIAL", ...],
      "oneaccordpt.com": ["YES|NO|PARTIAL", ...]
    }
  }
}

Make scores realistic: higher score = stronger competitor. Be specific and actionable. Focus especially on ${focusLabel}. Scores should reflect the ${focusLabel} focus area specifically.`;

  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 1000,
      tools: [{ type: 'web_search_20250305', name: 'web_search' }],
      messages: [{ role: 'user', content: prompt }]
    })
  });

  if (!response.ok) throw new Error(`API error: ${response.status}`);
  const data = await response.json();

  const text = data.content
    .filter(b => b.type === 'text')
    .map(b => b.text)
    .join('');

  const clean = text.replace(/```json|```/g, '').trim();
  const jsonStart = clean.indexOf('{');
  const jsonEnd = clean.lastIndexOf('}');
  if (jsonStart === -1) throw new Error('No JSON in response');
  return JSON.parse(clean.slice(jsonStart, jsonEnd + 1));
}

// ── Render report ──────────────────────────────────────────────────────────
function renderReport(data, focusLabel) {
  lastReport = data;

  // Scores
  renderGrid(data.scores);

  // Header
  document.getElementById('reportTitle').textContent = `Morning Intelligence Report — ${focusLabel}`;
  document.getElementById('reportMeta').textContent = `Generated ${new Date().toLocaleString()} · ${competitors.length} sites analyzed`;

  const badge = document.getElementById('threatBadge');
  badge.textContent = `Threat Level: ${data.overallThreat}`;
  badge.className = 'threat-badge ' + ({ HIGH: 'threat-high', MEDIUM: 'threat-med', LOW: 'threat-low' }[data.overallThreat] || 'threat-med');

  // Summary
  document.getElementById('insightBubble').innerHTML = data.executiveSummary.replace(/Modern Medicine/g, '<strong>Modern Medicine</strong>').replace(/Modern Women/g, '<strong>Modern Women</strong>');

  // Scores row
  const allSites = competitors.map(c => ({
    ...c,
    score: data.scores[c.url] || 0
  })).sort((a, b) => b.score - a.score);

  document.getElementById('scoresRow').innerHTML = allSites.map(c => `
    <div class="score-card ${c.isYou ? 'you-card' : ''}">
      <div class="score-card-name">${c.name}</div>
      <div class="score-card-num" style="color:${c.isYou ? 'var(--cyan)' : getScoreColor(c.score)}">${c.score}</div>
      <div class="score-card-label">/ 100</div>
    </div>`).join('');

  // New at competitors
  const severityOrder = { HIGH: 0, MEDIUM: 1, LOW: 2 };
  document.getElementById('newItems').innerHTML = (data.newAtCompetitors || []).map(item => `
    <div class="alert-item">
      <span class="alert-tag ${item.type === 'NEW' ? 'tag-new' : item.type === 'THREAT' ? 'tag-threat' : 'tag-improved'}">${item.type}</span>
      <div class="alert-content">
        <div class="alert-company">${item.company}</div>
        <div class="alert-text">${item.finding}</div>
        <div class="action-why" style="margin-top:4px">${item.impact}</div>
      </div>
    </div>`).join('') || '<div style="color:var(--text-muted);font-size:13px;padding:12px 0">No significant changes detected.</div>';

  // Threats
  const sorted = [...(data.whereTheyBeatUs || [])].sort((a,b) => (severityOrder[a.severity]||2) - (severityOrder[b.severity]||2));
  document.getElementById('threatItems').innerHTML = sorted.map(item => `
    <div class="alert-item">
      <span class="alert-tag tag-threat">${item.severity}</span>
      <div class="alert-content">
        <div class="alert-company">${item.company} · ${item.area}</div>
        <div class="alert-text">${item.finding}</div>
      </div>
    </div>`).join('') || '<div style="color:var(--text-muted);font-size:13px;padding:12px 0">No major threats identified.</div>';

  // Action plan
  document.getElementById('actionItems').innerHTML = (data.actionPlan || []).map(item => `
    <div class="action-item">
      <div class="priority-dot ${item.priority === 'URGENT' ? 'p-urgent' : item.priority === 'HIGH' ? 'p-high' : 'p-medium'}"></div>
      <div class="action-content">
        <div class="action-title">${item.title}</div>
        <div class="action-why">${item.why}</div>
        <div class="action-effort">⏱ ${item.effort} · Priority: ${item.priority}</div>
      </div>
    </div>`).join('');

  // Comparison matrix
  const matrix = data.comparisonMatrix;
  if (matrix) {
    const compNames = competitors.reduce((acc, c) => { acc[c.url] = c.name; return acc; }, {});
    const urls = Object.keys(matrix.data);
    let html = '<thead><tr><th>Feature</th>' + urls.map(u => `<th class="${u === 'getmodernmedicine.com' ? 'you-col' : ''}">${compNames[u] || u}</th>`).join('') + '</tr></thead><tbody>';
    matrix.features.forEach((feat, i) => {
      html += '<tr><td>' + feat + '</td>';
      urls.forEach(u => {
        const val = (matrix.data[u] || [])[i] || 'NO';
        const icon = val === 'YES' ? '<span class="check">✓</span>' : val === 'PARTIAL' ? '<span class="partial">◐</span>' : '<span class="cross">✗</span>';
        html += `<td class="${u === 'getmodernmedicine.com' ? 'you-col' : ''}">${icon} ${val}</td>`;
      });
      html += '</tr>';
    });
    html += '</tbody>';
    document.getElementById('compareTable').innerHTML = html;
  }

  document.getElementById('report').classList.add('visible');
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }
</script>
</body>
</html>
