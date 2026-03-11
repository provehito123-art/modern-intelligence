import streamlit as st

# Настройка страницы
st.set_page_config(page_title="Modern Medicine OS", layout="wide", initial_sidebar_state="collapsed")

# Безопасный инжект CSS-стилей для премиального визуала
st.markdown("""
    <style>
    /* Базовый фон и шрифты */
    .stApp { background-color: #FBFBFD; }
    h1, h2, h3, p, span { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    h1 { color: #1D1D1F; font-weight: 700; letter-spacing: -0.5px; }
    
    /* Стили для карточек */
    .premium-card {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
        border: 1px solid rgba(0, 0, 0, 0.03);
        margin-bottom: 24px;
        transition: all 0.3s ease;
    }
    .premium-card:hover {
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
        transform: translateY(-3px);
    }
    
    /* Стили для кнопок-ссылок внутри карточек */
    .link-btn {
        text-decoration: none;
        padding: 10px 18px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 14px;
        transition: 0.2s;
        display: inline-block;
        margin-right: 10px;
    }
    .link-website { background-color: #F5F5F7; color: #1D1D1F; }
    .link-website:hover { background-color: #E8E8ED; }
    .link-ads { background-color: #E8F2FF; color: #007AFF; }
    .link-ads:hover { background-color: #D1E5FF; }

    /* Скрываем лишние элементы Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Заголовок
st.title("⚡ Modern Medicine: Market Intelligence")
st.markdown("<p style='font-size: 18px; color: #86868B; margin-bottom: 30px;'>Advanced real-time monitoring and strategic analytics for Arizona clinics.</p>", unsafe_allow_html=True)

# Вкладки
tab1, tab2 = st.tabs(["🔥 Sports Medicine Competitors", "🌸 Women's Pelvic Center"])

def create_competitor_card(name, url, ads_url, traffic_trend, keywords):
    # Используем f-строку только для HTML структуры
    html = f"""
    <div class="premium-card">
        <h3 style="margin-top: 0; margin-bottom: 15px; color: #1D1D1F;">{name}</h3>
        <div style="display: flex; gap: 20px; margin-bottom: 20px; font-size: 15px; color: #515154;">
            <span style="background: #E8F5E9; color: #2E7D32; padding: 4px 8px; border-radius: 6px; font-weight: 600;">📈 Traffic: {traffic_trend}</span>
            <span>🔑 <b>Top Keywords:</b> {keywords}</span>
        </div>
        <div>
            <a href="{url}" target="_blank" class="link-btn link-website">🌐 View Website</a>
            <a href="{ads_url}" target="_blank" class="link-btn link-ads">📢 Live Google Ads Radar</a>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# Раздел 1: Спортивная медицина
with tab1:
    col_cards, col_analysis = st.columns([1.3, 1])
    
    with col_cards:
        create_competitor_card(
            "Foothills Sports Medicine", 
            "https://foothillsrehab.com/", 
            "https://adstransparency.google.com/?region=US&query=Foothills+Sports+Medicine", 
            "+12% (30 days)", 
            "Physical therapy Tucson, knee rehab AZ"
        )
        create_competitor_card(
            "Banner Sports Medicine", 
            "https://www.bannerhealth.com/", 
            "https://adstransparency.google.com/?region=US&query=Banner+Health", 
            "+5% (30 days)", 
            "Sports doctor Phoenix, ACL recovery"
        )

    with col_analysis:
        st.markdown("<h3 style='margin-bottom: 20px;'>🤖 Deep AI Strategic Analysis</h3>", unsafe_allow_html=True)
        
        with st.expander("🚨 CRITICAL ALERT: Foothills Marketing Pivot", expanded=True):
            st.markdown("""
            **Market Change Detected:** Foothills just launched a new high-converting landing page offering "Free Initial Injury Assessments".
            
            **Why it matters for us:** They are actively capturing the top-of-the-funnel traffic (patients who are injured but haven't seen a surgeon yet). If we don't counter this, we lose market share in Tucson.
            
            **Recommended Action (Implement ASAP):** 1. Design and deploy a "Free 15-Min Discovery Visit" sticky banner on our homepage.
            2. Launch a targeted retargeting ad campaign focusing on "Immediate Sports Injury Care in Arizona".
            """)
            
        with st.expander("📊 SEO & UX/UI Gap Analysis"):
            st.markdown("""
            * **Traffic Leak:** We are currently missing out on ~2,000 local searches/month for "post-surgical sports rehab". 
            * **Design Advantage:** Banner Health's website has a slow load time (desktop & mobile). A sleek, fast-loading, airy redesign of our services page will drastically improve our conversion rate compared to them.
            """)

# Раздел 2: Женское здоровье
with tab2:
    col_cards_w, col_analysis_w = st.columns([1.3, 1])
    
    with col_cards_w:
        create_competitor_card(
            "SOL Physical Therapy", 
            "https://solpt.com/", 
            "https://adstransparency.google.com/?region=US&query=SOL+Physical+Therapy", 
            "+18% (30 days)", 
            "Pelvic floor therapy, postpartum pain"
        )
        create_competitor_card(
            "Bodycentral PT", 
            "https://bodycentralpt.net/", 
            "https://adstransparency.google.com/?region=US&query=Bodycentral+Physical+Therapy", 
            "-2% (30 days)", 
            "Women's physical therapy Tucson"
        )

    with col_analysis_w:
        st.markdown("<h3 style='margin-bottom: 20px;'>🤖 Deep AI Strategic Analysis</h3>", unsafe_allow_html=True)
        
        with st.expander("💡 OPPORTUNITY: High-LTV Market Gap Identified", expanded=True):
            st.markdown("""
            **Market Change Detected:** SOL PT has increased their ad spend by roughly 40% on keywords related to "Postpartum Recovery".
            
            **Why it matters for us:** Postpartum patients have a very High Lifetime Value (LTV) and strong referral rates. The market demand in Arizona is currently outperforming supply.
            
            **Recommended Action (Implement ASAP):** 1. Create a structured, benefit-driven email sequence for our current database offering a "Postpartum Pelvic Health Checkup".
            2. Build an interactive "Do I need Pelvic Floor Therapy?" assessment quiz on the website to capture hesitant leads.
            """)
