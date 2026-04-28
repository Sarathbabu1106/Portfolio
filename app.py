import streamlit as st
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Sarath Babu | Portfolio", page_icon="🚀", layout="wide")

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOAD RESUME DATA ---
def get_pdf_display(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    return f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'

# --- SIDEBAR ---
with st.sidebar:
    st.title("Contact Info")
    st.write("📍 Tirupati, Andhra Pradesh [cite: 31]")
    st.write("📧 sarathbabu1106@gmail.com ")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/sarathbabu11) ")
    st.write("💻 [GitHub](https://github.com/Sarathbabu1106) ")
    st.write("---")
    st.write("🎓 **Class of 2026** [cite: 4]")
    
# --- HEADER ---
col_head1, col_head2 = st.columns([2, 1])
with col_head1:
    st.title("Yellamanda Sarath Babu")
    st.subheader("B.Tech AI/ML Student | Data Science & GenAI [cite: 4]")
    st.info("""
    I am a final-year Computer Science student specializing in AI/ML[cite: 4]. 
    I build end-to-end data pipelines [cite: 5], production-grade AI agents[cite: 6], 
    and DAX-driven BI dashboards[cite: 22].
    """)

# --- TABS FOR NAVIGATION ---
tab1, tab2, tab3 = st.tabs(["📂 Projects & Experience", "🛠️ Skills", "📄 Resume Viewer"])

with tab1:
    st.header("Featured Projects")
    
    # Project 1: AI Chatbot
    c1, c2 = st.columns([1, 2])
    with c1:
        st.write("**AI Personal Chatbot (Agentic RAG)**")
        st.caption("LangChain, Llama 3.3, ChromaDB [cite: 23, 24, 25]")
    with c2:
        st.write("""
        - Built a fully agentic assistant using ReAct Agent architecture[cite: 24].
        - Integrated 9 real-time APIs including F1 data and NewsAPI[cite: 26].
        - Implemented RAG for zero-hallucination document Q&A[cite: 25].
        """)

    st.write("---")

    # Project 2: Customer Churn
    c1, c2 = st.columns([1, 2])
    with c1:
        st.write("**Customer Churn Prediction & BI**")
        st.caption("Python, Scikit-Learn, Power BI [cite: 19]")
    with c2:
        st.write("""
        - Developed a Random Forest predictive system to identify high-risk customers[cite: 20].
        - Engineered a Python pipeline for real-time churn probability scores[cite: 21].
        - Designed a Power BI dashboard with heatmaps; isolated Fiber Optic users as key churn segment[cite: 22].
        """)

    st.header("Internship Experience")
    st.write(f"**Data Science Intern** | Codtech IT Solutions (May – Jul 2025) [cite: 12]")
    st.write("- Built automated predictive pipelines using Scikit-learn[cite: 13].")
    st.write(f"**BI Intern** | Excelr EdTech (Jun – Aug 2024) [cite: 15]")
    st.write("- Designed interactive dashboards using Power BI and Excel for business insights[cite: 16].")

with tab2:
    st.header("Technical Arsenal")
    k1, k2, k3 = st.columns(3)
    with k1:
        st.markdown("### Languages")
        st.write("Python, SQL, Java, JavaScript [cite: 8]")
    with k2:
        st.markdown("### AI / ML")
        st.write("LangChain, RAG, LLMs, Reinforcement Learning, TensorFlow [cite: 8]")
    with k3:
        st.markdown("### Data & BI")
        st.write("Power BI, Excel (Advanced), Tableau, Pandas, NumPy [cite: 9]")

with tab3:
    st.header("Resume")
    
    # Download Button
    with open("Sarath_Babu_Resume.pdf", "rb") as f:
        st.download_button(
            label="📥 Download Resume (PDF)",
            data=f,
            file_name="Sarath_Babu_Resume.pdf",
            mime="application/pdf"
        )
    
    # Resume Viewer (Iframe)
    try:
        resume_viewer = get_pdf_display("Sarath_Babu_Resume.pdf")
        st.markdown(resume_viewer, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Please ensure 'Sarath_Babu_Resume.pdf' is in the same directory as this script.")

# --- FOOTER ---
st.write("---")
st.caption("Developed by Sarath Babu | 2026 Grad")
