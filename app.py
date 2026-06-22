import streamlit as st
from data import ABOUT_FARMER, ABOUT_FARM, CROPS, PROFIT

st.set_page_config(page_title="Farmer AI Assistant", page_icon="🌾", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.main { background-color: #f4fff4; }

h1 { color: #1b5e20; text-align:center; }

.stButton>button {
    background-color: #2e7d32;
    color: white;
    height: 55px;
    font-size: 16px;
    border-radius: 10px;
}
.stButton>button:hover {
    background-color: #1b5e20;
}
</style>
""", unsafe_allow_html=True)

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- HOME ----------------
if st.session_state.page == "home":

    st.title("🌾 Farmer AI Assistant")
    st.subheader("Growing Knowledge, Cultivating the Future")

    st.markdown("### 📊 Farm Dashboard")

    c1, c2, c3 = st.columns(3)
    c1.metric("🌍 Farm Size", "40 Acres")
    c2.metric("🌱 Crops", "Wheat, Cotton, Maize")
    c3.metric("🥭 Orchard", "Guava, Mango, Orange")

    st.markdown("### 📂 Sections")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👨‍🌾 About Farmer", use_container_width=True):
            st.session_state.page = "farmer"

        if st.button("🚜 Our Farm", use_container_width=True):
            st.session_state.page = "farm"

    with col2:
        if st.button("🌾 Crops", use_container_width=True):
            st.session_state.page = "crops"

        if st.button("📈 Profit & Loss", use_container_width=True):
            st.session_state.page = "profit"

# ---------------- FARMER ----------------
elif st.session_state.page == "farmer":
    st.title("👨‍🌾 About Farmer")

    for q, a in ABOUT_FARMER.items():
        with st.expander(q):
            st.write(a)

    if st.button("⬅ Back"):
        st.session_state.page = "home"

# ---------------- FARM ----------------
elif st.session_state.page == "farm":
    st.title("🚜 Our Farm")

    for q, a in ABOUT_FARM.items():
        with st.expander(q):
            st.write(a)

    if st.button("⬅ Back"):
        st.session_state.page = "home"

# ---------------- CROPS ----------------
elif st.session_state.page == "crops":
    st.title("🌾 Crops Information")

    for q, a in CROPS.items():
        with st.expander(q):
            st.write(a)

    if st.button("⬅ Back"):
        st.session_state.page = "home"

# ---------------- PROFIT ----------------
elif st.session_state.page == "profit":
    st.title("📈 Profit & Loss")

    for q, a in PROFIT.items():
        with st.expander(q):
            st.write(a)

    if st.button("⬅ Back"):
        st.session_state.page = "home"