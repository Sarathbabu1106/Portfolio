import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Sarath Babu | Portfolio", page_icon="🚀", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("Contact Details")
    st.write("📍 Tirupati, Andhra Pradesh")
    st.write("📧 sarathbabu1106@gmail.com")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/sarathbabu11)")
    st.write("💻 [GitHub](https://github.com/Sarathbabu1106)")
    st.write("---")
    st.write("🎓 **Class of 2026**")
    st.write("🎯 Available for Relocation")

# --- HEADER ---
st.title("Yellamanda Sarath Babu")
st.subheader("B.Tech AI/ML Student | Machine Learning & GenAI Specialist")
st.write("Proficient in building end-to-end data pipelines using Python, SQL, and Power BI.")
st.write("Experienced in developing production-grade AI agents and predictive models.")

st.divider()

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📂 Projects & Experience", "🛠️ Technical Skills", "📄 Resume"])

with tab1:
    st.header("Featured Projects")
    
    with st.expander("🤖 AI Personal Chatbot – Agentic RAG Assistant", expanded=True):
        st.write("**Tech:** LangChain, Llama 3.3, ChromaDB")
        st.write("- Built a fully agentic assistant using ReAct Agent architecture.")
        st.write("- Integrated 9 real-time APIs including F1 data and NewsAPI.")
        st.write("- Implemented RAG for zero-hallucination document Q&A.")

    with st.expander("📊 Customer Churn Prediction & BI Dashboard"):
        st.write("**Tech:** Python, Scikit-Learn, Power BI")
        st.write("- Developed a Random Forest predictive system to identify high-risk customers.")
        st.write("- Engineered a Python pipeline for real-time churn probability scores.")
        st.write("- Designed Power BI dashboard with heatmaps identifying key churn segments.")

    st.header("Internship Experience")
    st.write("**Data Science Intern** | Codtech IT Solutions (May – Jul 2025)")
    st.write("- Built automated predictive pipelines using Scikit-learn.")
    st.write("**Business Intelligence Intern** | Excelr EdTech (Jun – Aug 2024)")
    st.write("- Designed interactive dashboards using Power BI and Excel.")

with tab2:
    st.header("Technical Arsenal")
    k1, k2 = st.columns(2)
    with k1:
        st.markdown("### AI / ML & Languages")
        st.write("Python, SQL, LangChain, RAG, Reinforcement Learning, Scikit-learn")
    with k2:
        st.markdown("### Data & Web")
        st.write("Power BI, Tableau, Excel (Advanced), MERN Stack, Streamlit, MySQL")

with tab3:
    st.header("Resume")
    
    col_res1, col_res2 = st.columns([1, 4])
    with col_res1:
        # Professional PDF Icon
        st.image("https://cdn-icons-png.flaticon.com/512/4726/4726010.png", width=100)
        
    with col_res2:
        st.subheader("Yellamanda Sarath Babu - Resume")
        st.write("Final Year B.Tech CSE (AI & ML)")
        st.write("Click the button below to download the latest version of my resume.")
        
        # Simple Download Button
        try:
            with open("static/Sarath_Babu_Resume.pdf", "rb") as f:
                st.download_button(
                    label="📥 Download Resume (PDF)",
                    data=f,
                    file_name="Sarath_Babu_Resume.pdf",
                    mime="application/pdf"
                )
        except FileNotFoundError:
            st.error("Resume file not found. Please ensure 'Sarath_Babu_Resume.pdf' is inside the 'static' folder.")

st.divider()
st.caption("© 2026 Sarath Babu | Built with Streamlit")
