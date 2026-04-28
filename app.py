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
    st.write("🎯 **Available for Relocation**")
    
# --- HEADER ---
st.title("Yellamanda Sarath Babu")
st.subheader("B.Tech AI/ML (Class of 2026) | Machine Learning & GenAI Specialist")
st.write("Proficient in building end-to-end data pipelines using Python, SQL, and Power BI.")
st.write("Experienced in developing production-grade AI agents and predictive models.")

st.divider()

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📂 Projects & Experience", "🛠️ Technical Skills", "📄 Resume"])

with tab1:
    st.header("Featured Projects")
    
    with st.expander("🤖 AI Personal Chatbot – Agentic RAG Assistant", expanded=True):
        st.write("**Tech:** LangChain, LLMs")
        st.write("- Built a fully agentic assistant using LangChain ReAct Agent and Llama 3.3 (70B).")
        st.write("- Integrated 9 real-time APIs including OpenWeatherMap, NewsAPI, and F1 data.")
        st.write("- Implemented RAG with Google Gemini Embeddings and ChromaDB for zero-hallucination document Q&A.")

    with st.expander("📊 Customer Churn Prediction & BI Dashboard"):
        st.write("**Tech:** Python, Scikit-Learn, Power BI")
        st.write("- Built predictive system using Random Forest to identify high-risk customers.")
        st.write("- Engineered Python pipeline to calculate real-time Churn Probability scores.")
        st.write("- Designed Power BI dashboard isolating Fiber Optic users as key churn segment.")

    st.header("Work History")
    st.write("**Data Science Intern** | Codtech IT Solutions (May – Jul 2025)")
    st.write("- Built automated predictive pipelines and optimized model performance.")
    st.write("**Business Intelligence Intern** | Excelr EdTech (Jun – Aug 2024)")
    st.write("- Designed interactive dashboards using Power BI and Excel to derive business insights.")

with tab2:
    st.header("Technical Arsenal")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Languages:** Python, SQL, Java, JavaScript")
        st.write("**AI/ML:** TensorFlow, Scikit-learn, LangChain, RAG, LLMs, Reinforcement Learning")
    with col2:
        st.write("**Data & BI:** Power BI, Tableau, Excel (Advanced), Pandas, NumPy")
        st.write("**Web & DB:** MERN Stack, Streamlit, MySQL, ChromaDB")

with tab3:
    st.header("Resume")
    
    # 1. Update this URL with your Google Drive or GitHub link
    RESUME_EXTERNAL_URL = "YOUR_RESUME_URL_HERE" 
    # 2. Keep this for the download button
    local_path = "static/Sarath_Babu_Resume.pdf"
    
    col_res1, col_res2 = st.columns([1, 3])
    with col_res1:
        st.image("https://cdn-icons-png.flaticon.com/512/4726/4726010.png", width=100)
        
    with col_res2:
        st.subheader("Yellamanda Sarath Babu - Resume")
        st.write("Final Year B.Tech CSE (AI & ML)")
        
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            st.markdown(f'''
                <a href="{RESUME_EXTERNAL_URL}" target="_blank" style="text-decoration: none;">
                    <button style="width: 100%; background-color: #007bff; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">
                        📄 View Full Screen
                    </button>
                </a>
            ''', unsafe_allow_html=True)
            
        with btn_col2:
            try:
                with open(local_path, "rb") as f:
                    st.download_button(label="📥 Download PDF", data=f, file_name="Sarath_Babu_Resume.pdf", mime="application/pdf")
            except FileNotFoundError:
                st.error("Local file not found in 'static' folder.")

st.divider()
st.caption("© 2026 Sarath Babu | Built with Streamlit")
