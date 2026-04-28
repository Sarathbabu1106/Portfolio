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
st.write("""
Proficient in building end-to-end data pipelines using Python, SQL, and Power BI[cite: 4, 5]. 
Experienced in developing production-grade AI agents and predictive models[cite: 6].
""")

st.divider()

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📂 Projects & Experience", "🛠️ Technical Skills", "📄 Resume"])

with tab1:
    st.header("Featured Projects")
    
    # Project 1: AI Chatbot
    with st.expander("🤖 AI Personal Chatbot – Agentic RAG Assistant", expanded=True):
        st.write("**Tech:** LangChain, LLMs [cite: 23]")
        st.write("- Built a fully agentic assistant using LangChain ReAct Agent and Llama 3.3 (70B)[cite: 24].")
        st.write("- Integrated 9 real-time APIs including OpenWeatherMap, NewsAPI, and F1 data[cite: 26].")
        st.write("- Implemented RAG with Google Gemini Embeddings and ChromaDB for zero-hallucination document Q&A[cite: 25].")

    # Project 2: Customer Churn
    with st.expander("📊 Customer Churn Prediction & BI Dashboard"):
        st.write("**Tech:** Python, Scikit-Learn, Power BI [cite: 19]")
        st.write("- Built predictive system using Random Forest to identify high-risk customers[cite: 20].")
        st.write("- Engineered Python pipeline to calculate real-time Churn Probability scores[cite: 21].")
        st.write("- Designed Power BI dashboard isolating Fiber Optic users as key churn segment[cite: 22].")

    st.header("Work History")
    st.write("**Data Science Intern** | Codtech IT Solutions (May – Jul 2025) [cite: 12]")
    st.write("- Built automated predictive pipelines and optimized model performance[cite: 13, 14].")
    
    st.write("**Business Intelligence Intern** | Excelr EdTech (Jun – Aug 2024) [cite: 15]")
    st.write("- Designed interactive dashboards using Power BI and Excel to derive business insights[cite: 16].")

with tab2:
    st.header("Technical Arsenal")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Languages:** Python, SQL, Java, JavaScript [cite: 8]")
        st.write("**AI/ML:** TensorFlow, Scikit-learn, LangChain, RAG, LLMs, Reinforcement Learning [cite: 8]")
    with col2:
        st.write("**Data & BI:** Power BI, Tableau, Excel (Advanced), Pandas, NumPy [cite: 9]")
        st.write("**Web & DB:** MERN Stack, Streamlit, MySQL, ChromaDB [cite: 10]")

with tab3:
    st.header("Resume")
    
    # Path to your file inside the static folder
    resume_path = "static/Sarath_Babu_Resume.pdf"
    
    col_res1, col_res2 = st.columns([1, 3])
    
    with col_res1:
        # A simple PDF icon
        st.image("https://cdn-icons-png.flaticon.com/512/4726/4726010.png", width=100)
        
    with col_res2:
        st.subheader("Yellamanda Sarath Babu - Resume")
        st.write("Final Year B.Tech CSE (AI & ML) [cite: 4, 31]")
        
        btn_col1, btn_col2 = st.columns(2)
        
        with btn_col1:
            # Bulletproof: Opens the PDF directly in a new tab
            st.markdown(f'''
                <a href="{resume_path}" target="_blank" style="text-decoration: none;">
                    <button style="
                        width: 100%;
                        background-color: #007bff;
                        color: white;
                        padding: 10px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        font-weight: bold;">
                        📄 View Full Screen
                    </button>
                </a>
            ''', unsafe_allow_html=True)
            
        with btn_col2:
            # Standard Streamlit Download Button
            try:
                with open(resume_path, "rb") as f:
                    st.download_button(
                        label="📥 Download PDF",
                        data=f,
                        file_name="Sarath_Babu_Resume.pdf",
                        mime="application/pdf"
                    )
            except FileNotFoundError:
                st.error("File not found. Ensure the resume is in the 'static' folder.")

# --- FOOTER ---
st.divider()
st.caption("© 2026 Sarath Babu | Built with Streamlit")
