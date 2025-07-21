import streamlit as st
import re
import pandas as pd
from datetime import date
from fpdf import FPDF
import os

# ------------------ Page Setup ------------------
st.set_page_config(page_title="User Info Form", layout="centered")

# ------------------ Custom CSS for Background ------------------
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=1470&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .block-container {
        background-color: rgba(255, 244, 229, 0.92);  /* Warm beige background */
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15); /* Optional shadow for depth */
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ Title ------------------
st.markdown("<h2 style='text-align: center; color: #D2691E;'>📝 User Information Form</h2>", unsafe_allow_html=True)
st.markdown("Please enter your details below and click Submit.")
st.markdown("---")

# ------------------ DOB Age Limit ------------------
today = date.today()
min_dob = date(1900, 1, 1)
max_dob = date(today.year - 18, today.month, today.day)

# ------------------ Validation Function ------------------
def validate_input(pattern, text):
    return re.fullmatch(pattern, text)

# ------------------ PDF Generator ------------------
def generate_pdf(name, dob, email, mobile):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="User Info Receipt", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"DOB: {dob}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Mobile: {mobile}", ln=True)
    filename = "user_receipt.pdf"
    pdf.output(filename)
    return filename

# ------------------ Form ------------------
with st.form("user_form"):
    st.markdown("### ✨ Your Details")
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("👤 Full Name", placeholder="e.g., John Doe")
        dob = st.date_input("📅 Date of Birth", min_value=min_dob, max_value=max_dob)
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        st.info(f"🎂 Your Age: {age} years")

    with col2:
        email = st.text_input("📧 Email ID", placeholder="e.g., example@gmail.com")
        mobile = st.text_input("📞 Mobile Number", placeholder="10-digit number")

    submitted = st.form_submit_button("🚀 Submit")

# ------------------ Validation ------------------
name_valid = validate_input(r'^[A-Za-z ]+$', name)
email_valid = validate_input(r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$', email)
mobile_valid = validate_input(r'^[0-9]{10}$', mobile)
dob_str = dob.strftime("%m-%d-%Y")

# ------------------ Submission Handling ------------------
if submitted:
    if dob > max_dob:
        st.warning("⚠️ You must be at least 18 years old.")
    elif all([name_valid, email_valid, mobile_valid]):
        st.success("✅ All details are valid!")

        # Show Submitted Info
        st.markdown(f"**👤 Name:** `{name}`")
        st.markdown(f"**📅 DOB:** `{dob_str}`")
        st.markdown(f"**📧 Email:** `{email}`")
        st.markdown(f"**📞 Mobile:** `{mobile}`")

        # CSV Download
        data = {
            "Name": [name],
            "DOB": [dob_str],
            "Email": [email],
            "Mobile": [mobile]
        }
        df = pd.DataFrame(data)
        st.download_button("⬇️ Download Info as CSV", df.to_csv(index=False), file_name="user_info.csv")

        # PDF Download
        pdf_file = generate_pdf(name, dob_str, email, mobile)
        with open(pdf_file, "rb") as f:
            st.download_button("📄 Download PDF Receipt", f, file_name="user_info.pdf", mime="application/pdf")

    else:
        st.error("⚠️ Some fields are invalid. Please fix them below.")
        if not name_valid:
            st.warning("🔴 Name should contain only letters and spaces.")
        if not email_valid:
            st.warning("🔴 Email format should be like example@gmail.com")
        if not mobile_valid:
            st.warning("🔴 Mobile number must be 10 digits.")
