import streamlit as st
st.set_page_config(
    page_title="FWI Prediction",
    page_icon="🔥",
    layout="wide"
)

st.markdown("""
<style>
.hero{
    padding:50px;
    border-radius:20px;
    background:linear-gradient(135deg,#ff4b4b,#ff8c42);
    color:white;
    text-align:center;
}

.feature{
    padding:20px;
    border-radius:15px;
    background:#f5f5f5;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🔥 Forest Fire Weather Index Prediction</h1>
    <h3>Machine Learning Powered Forest Fire Risk Assessment</h3>
    <p>Predict forest fire danger using environmental parameters.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature">
        <h3>🌡 Weather Data</h3>
        <p>Analyze temperature and humidity.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature">
        <h3>🤖 ML Model</h3>
        <p>Powered by trained Ridge Regression Model.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature">
        <h3>🔥 Fire Risk</h3>
        <p>Get instant FWI predictions.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.subheader("📖 About Project")

st.write("""
The Forest Fire Weather Index (FWI) is a numerical rating of fire intensity.

This application predicts the FWI using:

- Temperature
- Relative Humidity
- Wind Speed
- Rainfall
- FFMC
- DMC
- ISI
- Region
- Fire Classes

👉 Use the sidebar and open **FWI Prediction** page.
""")
