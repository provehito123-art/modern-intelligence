import streamlit as st

# Page configuration
st.set_page_config(page_title="Modern Medicine Hub", layout="wide", initial_sidebar_state="collapsed")

# Apple-style UI CSS for a clean, premium look
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .css-1n76uvr { background-color: #f5f5f7; border-radius: 20px; }
    .metric-card {
        background: #f5f5f7;
        padding: 20px;
        border-radius: 18px;
        border: 1px solid #e5e5e7;
        transition: 0.3s;
    }
    .metric-card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.05); }
    h1, h2, h3 { font-family: 'SF Pro Display', -apple-system, sans-serif; color: #1d1d1f; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏥 Market Intelligence Dashboard")
st.subheader("Strategic Clinic Monitoring in Arizona")

col1, col2 = st.columns([2, 1])

with col1:
    tab1, tab2 = st.tabs(["🔥 Sports Medicine", "🌸 Pelvic Health"])

    def competitor_box(name, site, ads, maps, score):
        with st.container():
            st.markdown(f"""
            <div class="metric-card">
                <div style="display: flex; justify-content: space-between;">
                    <h3>{name}</h3>
                    <span style="color: #007AFF; font-weight: bold;">SEO Score: {score}%</span>
                </div>
                <p>📍 <b>Location:</b> Arizona (Tucson/Phoenix)</p>
                <a href="{site}" target="_blank">🌐 Website</a> | 
                <a href="{ads}" target="_blank">📢 Google Ads</a> | 
                <a href="{maps}" target="_blank">📍 Maps</a>
            </div><br>
            """, unsafe_allow_html=True)

    with tab1:
        competitor_box("Foothills Sports Medicine", "https://foothillsrehab.com/", "https://adstransparency.google.com/?region=US&query=Foothills+Sports+Medicine", "https://www.google.com/maps/search/Foothills+Sports+Medicine+Arizona", 88)
        competitor_box("Banner Sports Medicine", "https://www.bannerhealth.com/", "https://adstransparency.google.com/?region=US&query=Banner+Health", "https://www.google.com/maps/search/Banner+Sports+Medicine+Arizona", 94)
        
        if st.button("🚀 Run AI Analysis (Sports)"):
            st.info("💡 **AI INSIGHT:** Competitors have increased ad spend on the keyword 'Physical Therapy Tucson'. Recommendation: Update our hero section to 'Top-Rated Sports PT in Tucson' to boost CTR.")

    with tab2:
        competitor_box("SOL Physical Therapy", "https://solpt.com/", "https://adstransparency.google.com/?region=US&query=SOL+Physical+Therapy", "https://www.google.com/maps/search/SOL+Physical+Therapy+Arizona", 82)
        competitor_box("Bodycentral PT", "https://bodycentralpt.net/", "https://adstransparency.google.com/?region=US&query=Bodycentral+Physical+Therapy", "https://www.google.com/maps/search/Bodycentral+Physical+Therapy+Arizona", 79)
        
        if st.button("✨ Run AI Analysis (Pelvic)"):
            st.success("🎯 **AI INSIGHT:** Bodycentral is missing a dedicated 'Postpartum Exercise' section. If we launch a targeted landing page tomorrow, we can capture this search traffic in Arizona within 2 weeks.")

with col2:
    st.markdown("""<div class="metric-card"><h3>📈 Our Status</h3>""", unsafe_allow_html=True)
    st.progress(90, text="SEO Optimization")
    st.progress(75, text="Ads Performance")
    st.progress(60, text="Market Share (AZ)")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.write("---")
    if st.button("📋 Generate Executive Report"):
        st.code("Summary: We are leading in content quality, but Banner Health outspends us in Phoenix. Action plan: Increase Google Ads budget by 15% for targeted keywords.", language="text")
