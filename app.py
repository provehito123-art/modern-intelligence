import streamlit as st

# Basic page setup
st.set_page_config(page_title="Modern Medicine Hub", layout="wide")

# Safe CSS injection for a clean, minimalist look
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .competitor-card {
        background-color: #F8F9FA;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #E0E0E0;
        margin-bottom: 15px;
    }
    h1, h2, h3 { color: #1D1D1F; font-family: 'Helvetica Neue', sans-serif; }
    .stButton>button { border-radius: 10px; background-color: #007AFF; color: white; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏥 Market Intelligence Dashboard")
st.write("Strategic analytics for Arizona clinics.")

# Two columns: Main Content and Our Status
col_main, col_stats = st.columns([2, 1])

with col_main:
    tab1, tab2 = st.tabs(["🔥 Sports Medicine", "🌸 Pelvic Health"])

    def display_competitor(name, site, ads, score):
        st.markdown(f"""
        <div class="competitor-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h3 style="margin: 0;">{name}</h3>
                <span style="color: #007AFF; font-weight: bold;">SEO Score: {score}%</span>
            </div>
            <p style="margin: 10px 0;">📍 Location: Arizona (Tucson / Phoenix)</p>
            <a href="{site}" target="_blank">🌐 Website</a> | 
            <a href="{ads}" target="_blank">📢 View Active Ads</a>
        </div>
        """, unsafe_allow_html=True)

    with tab1:
        display_competitor("Foothills Sports Medicine", "https://foothillsrehab.com/", "https://adstransparency.google.com/?region=US&query=Foothills+Sports+Medicine", 88)
        display_competitor("Banner Sports Medicine", "https://www.bannerhealth.com/", "https://adstransparency.google.com/?region=US&query=Banner+Health", 94)
        
        if st.button("Analyze Sports Market Trends"):
            st.info("💡 **AI INSIGHT:** Local competitors are focusing on 'Low Back Pain' keywords this week. We should prioritize our 'Spine Care' content to stay ahead.")

    with tab2:
        display_competitor("SOL Physical Therapy", "https://solpt.com/", "https://adstransparency.google.com/?region=US&query=SOL+Physical+Therapy", 82)
        display_competitor("Bodycentral PT", "https://bodycentralpt.net/", "https://adstransparency.google.com/?region=US&query=Bodycentral+Physical+Therapy", 79)
        
        if st.button("Analyze Pelvic Health Trends"):
            st.success("🎯 **AI INSIGHT:** 'Postpartum Rehab' is trending in Tucson. Launching a 3-part Instagram series could capture this niche before SOL PT scales up.")

with col_stats:
    st.markdown("### 📈 Internal Performance")
    st.progress(90, text="SEO Health")
    st.progress(75, text="Ad Efficiency")
    st.progress(60, text="Market Share (AZ)")
    
    st.divider()
    if st.button("📋 Copy Executive Summary"):
        st.code("Summary: We lead in SEO, but need more aggressive Ad spend in Phoenix to match Banner Health. Suggested action: 15% budget reallocation.", language="text")
