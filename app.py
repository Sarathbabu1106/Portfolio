import streamlit as st
import base64

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

# --- PDF VIEWER FUNCTION ---
def get_pdf_display(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    return f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'

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
st.write("""
Proficient in building end-to-end data pipelines using Python, SQL, and Power BI. 
Experienced in developing production-grade AI agents and predictive models.
""")

st.divider()

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📂 Projects & Experience", "🛠️ Technical Skills", "📄 Resume Viewer"])

with tab1:
    st.header("Featured Projects")
    
    # Project 1
    with st.expander("🤖 AI Personal Chatbot – Agentic RAG Assistant", expanded=True):
        st.write("**Tech:** LangChain, Llama 3.3, ChromaDB")
        st.write("- Built a fully agentic assistant using ReAct Agent architecture and Llama 3.3 (70B).")
        st.write("- Integrated 9 real-time APIs including OpenWeatherMap, NewsAPI, and F1 data.")
        st.write("- Implemented RAG with Gemini Embeddings for zero-hallucination document Q&A.")

    # Project 2
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
        st.write("**AI/ML:** TensorFlow, Scikit-learn, LangChain, RAG, Reinforcement Learning")
    with col2:
        st.write("**Data & BI:** Power BI, Tableau, Excel (Advanced), Pandas, NumPy")
        st.write("**Web & DB:** MERN Stack, Streamlit, MySQL, ChromaDB")

with tab3:
    st.header("Resume")
    
    # Check for PDF file and display
    try:
        with open("Sarath_Babu_Resume.pdf", "rb") as f:
            st.download_button(
                label="📥 Download My Resume (PDF)",
                data=f,
                file_name="Sarath_Babu_Resume.pdf",
                mime="application/pdf"
            )
        
        st.markdown(get_pdf_display("Sarath_Babu_Resume.pdf"), unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Please upload 'Sarath_Babu_Resume.pdf' to your repository to enable the viewer.")

# --- FOOTER ---
st.divider()
st.caption("© 2026 Sarath Babu | Built with Streamlit")
