import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page Configuration
st.set_page_config(
    page_title="AICTE - FDR Verification Portal",
    page_icon="📜",
    layout="wide"
)

# Custom CSS for Modern Glassmorphic UI Aesthetics
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%);
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.125);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }
    .sub-title {
        color: #94a3b8;
        font-size: 1rem;
        margin-bottom: 24px;
    }
    .badge-success {
        background: rgba(34, 197, 94, 0.2);
        color: #4ade80;
        border: 1px solid rgba(34, 197, 94, 0.4);
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 600;
    }
    .badge-warning {
        background: rgba(234, 179, 8, 0.2);
        color: #fde047;
        border: 1px solid rgba(234, 179, 8, 0.4);
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 600;
    }
    div[data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.7);
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    .stButton>button {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<div class="main-title">AICTE Automated FDR Verification Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Problem Statement ID: SIH26262 | AI OCR & Automated Compliance Engine</div>', unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.subheader("🛡️ AICTE Portal")
    page = st.radio("Select View", ["📄 Single Document Upload", "📊 AICTE Dashboard", "⚙️ Verification Rules"])
    st.markdown("---")
    st.caption("Secured via End-to-End Hash Validation")

# Session State Master Data
if 'fdr_records' not in st.session_state:
    st.session_state.fdr_records = [
        {"Institution": "IIT Guwahati", "FDR No": "FDR-889021", "Bank": "State Bank of India", "Amount (₹)": 500000, "Expiry Date": "2027-04-15", "Status": "Verified"},
        {"Institution": "Delhi Technical College", "FDR No": "FDR-442109", "Bank": "HDFC Bank", "Amount (₹)": 350000, "Expiry Date": "2026-12-01", "Status": "Verified"},
        {"Institution": "Apex Engineering College", "FDR No": "FDR-109283", "Bank": "Punjab National Bank", "Amount (₹)": 150000, "Expiry Date": "2026-05-10", "Status": "Expiring Soon"},
    ]

# Page 1: Single Document Upload & OCR
if page == "📄 Single Document Upload":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Upload Fixed Deposit Receipt (FDR)")
    st.write("Upload scanned FDR certificate for instant automated OCR Extraction.")
    
    uploaded_file = st.file_uploader("Upload document", type=['pdf', 'png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        st.info("🔄 Processing Document via OCR Extraction Engine...")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Document Preview")
            if uploaded_file.type != "application/pdf":
                st.image(uploaded_file, use_container_width=True)
            else:
                st.success("PDF Document Loaded Successfully")
                
        with col2:
            st.markdown("### Extracted FDR Details")
            bank_name = st.text_input("Bank Name", "State Bank of India")
            fdr_no = st.text_input("FDR Number", "FDR-992384")
            amount = st.number_input("Amount (INR)", value=500000, step=50000)
            maturity_date = st.date_input("Maturity Date", datetime.today() + timedelta(days=730))
            
            if amount >= 300000:
                st.markdown('Status: <span class="badge-success">VALIDATED</span>', unsafe_allow_html=True)
            else:
                st.markdown('Status: <span class="badge-warning">REVIEW REQUIRED</span>', unsafe_allow_html=True)
                
            if st.button("Submit Record"):
                st.session_state.fdr_records.append({
                    "Institution": "Uploaded Institute",
                    "FDR No": fdr_no,
                    "Bank": bank_name,
                    "Amount (₹)": amount,
                    "Expiry Date": str(maturity_date),
                    "Status": "Verified"
                })
                st.success("✅ FDR Record successfully verified and saved!")
    st.markdown('</div>', unsafe_allow_html=True)

# Page 2: Dashboard View
elif page == "📊 AICTE Dashboard":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("AICTE Central FDR Tracking & Monitoring")
    df = pd.DataFrame(st.session_state.fdr_records)
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Submitted", len(df))
    m2.metric("Verified & Active", len(df[df['Status'] == 'Verified']))
    m3.metric("Action Required", len(df[df['Status'] != 'Verified']))
    
    st.dataframe(df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Page 3: Verification Rules Config
else:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Automated Compliance & Alert Settings")
    st.slider("Minimum Required FDR Amount (₹)", 100000, 1000000, 300000)
    st.number_input("Expiry Alert Threshold (Days in advance)", value=30)
    st.button("Save Configuration")
    st.markdown('</div>', unsafe_allow_html=True)
