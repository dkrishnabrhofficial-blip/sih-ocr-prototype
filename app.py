import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="AICTE FDR Verification Portal", page_icon="🏛️", layout="wide")

st.title("🏛️ AICTE FDR Automated Verification & Expiry Portal")
st.markdown("---")

# Sidebar Navigation
menu = st.sidebar.selectbox("Navigation", ["Institution Upload", "AICTE Admin Dashboard"])

if menu == "Institution Upload":
    st.header("📄 Upload Fixed Deposit Receipt (FDR)")
    
    institution_name = st.text_input("Enter Institution Name", "ABC Institute of Technology & Management")
    uploaded_file = st.file_uploader("Upload FDR Document (Image/PDF)", type=["png", "jpg", "jpeg", "pdf"])

    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        st.image(uploaded_file, caption="Uploaded FDR Preview", width=350)
        
        if st.button("Run OCR & Verify Document"):
            with st.spinner("Extracting text and verifying details via OCR..."):
                # Mock extracted details for the prototype demo
                extracted_bank = "State Bank of India (SBI)"
                extracted_amount = "₹ 50,00,000"
                extracted_date = "2027-12-15"
                
                st.subheader("🔍 Extracted OCR Details:")
                st.write(f"**Bank Name:** {extracted_bank}")
                st.write(f"**FDR Amount:** {extracted_amount}")
                st.write(f"**Expiry Date:** {extracted_date}")
                
                # Validation Logic
                expiry_dt = datetime.strptime(extracted_date, "%Y-%m-%d")
                if expiry_dt > datetime.now():
                    st.success("Verification Status: VALID ✅ (Secure & Active)")
                else:
                    st.error("Verification Status: EXPIRED ❌ (Renewal Required)")

elif menu == "AICTE Admin Dashboard":
    st.header("📊 AICTE Central Admin Monitoring Dashboard")
    
    # Quick Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Submissions", "1,245")
    col2.metric("Valid FDRs", "1,120")
    col3.metric("Expired / Alerts", "125")
    
    st.markdown("---")
    st.subheader("📋 Affiliated Institutions FDR Status List")
    
    # Mock database table
    data = {
        "Institution": ["ABC Engineering College", "XYZ Global Management", "PQR Institute of Tech", "Global Sciences"],
        "Bank": ["SBI", "HDFC Bank", "ICICI Bank", "Axis Bank"],
        "Amount": ["₹ 50 Lakhs", "₹ 25 Lakhs", "₹ 1 Cr", "₹ 40 Lakhs"],
        "Expiry Date": ["2027-05-12", "2026-01-10", "2028-11-20", "2025-08-15"],
        "Status": ["Valid ✅", "Expired ❌", "Valid ✅", "Expired ❌"]
    }
    df = pd.DataFrame(data)
    
    st.dataframe(df, use_container_width=True)
