import streamlit as st

st.set_page_config(
    page_title="Hospital Dashboard",
    page_icon="📊",
    layout="wide"
)

# Remove Streamlit's default spacing
st.markdown("""
<style>
    .block-container {
        padding: 0rem;
        max-width: 100%;
    }
</style>
""", unsafe_allow_html=True)

powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=e0f338b2-e71e-4bf3-b8ab-5cad9a3f4a29&autoAuth=true&ctid=9c57347d-760c-410c-8ea1-f1c42e38522d&theme=light"

st.iframe(
    powerbi_url,
    width="stretch",
    height=1000
)