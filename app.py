
import streamlit as st
from modules.input_forms import get_user_inputs
from modules.tax_logic import estimate_tax
from modules.export_utils import generate_csv
from datetime import datetime
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="TaxMate - Smart Tax Assistant", layout="centered")

# --- Header ---
st.title("🇳🇱 TaxMate - Smart Tax Assistant")
st.markdown("Making Dutch tax filing easier for freelancers, students, and employees.")

# --- Simulate official data portal ---
with st.expander("🔐 Connect to Belastingdienst (Simulation)"):
    st.info("Connect to DigiD or Mijn Belastingdienst to fetch official data. [Simulation Mode]")
    if st.button("Simulate Connection to Tax Office"):
        with st.spinner("Connecting securely..."):
            time.sleep(2)
        st.success("✅ Connected! 2023 income: €41,500, VAT filed: €6,100.")

# --- Tabs for different user types ---
tabs = st.tabs(["Freelancer / ZZP", "Student", "Employee", "For Companies"])

# --- ZZP Tab ---
with tabs[0]:
    st.header("💼 Tax Estimator for Freelancers (ZZP)")
    st.info("""
You are considered a **Freelancer (ZZP)** in the Netherlands if:
- You work for yourself and don’t employ staff.
- You send invoices to clients for your work (e.g. designer, translator, developer).
- You’re responsible for reporting your income and paying taxes.
- You may be eligible for **tax deductions** like the zelfstandigenaftrek.
""")

    inputs = get_user_inputs(role="zzp")

    if st.button("Estimate My Taxes"):
        results = estimate_tax(inputs)
        st.subheader("📊 Tax Estimation Result")

        col1, col2 = st.columns(2)
        col1.metric(label="Estimated Income Tax", value=f"€ {results['income_tax']:.2f}")
        col2.metric(label="Estimated VAT to Pay", value=f"€ {results['vat']:.2f}")

        st.subheader("📉 Deductions Applied")
        if results['deductions']:
            for d in results['deductions']:
                st.markdown(f"✅ {d}")
        else:
            st.write("No deductions applied.")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"tax_estimate_{timestamp}.csv"

        st.download_button(
            label="📥 Download Report as CSV",
            data=generate_csv(inputs, results),
            file_name=filename,
            mime="text/csv"
        )

    with st.expander("📤 Request Human Expert Review"):
        st.write("Upload your payslip or tax report for manual checking.")
        uploaded = st.file_uploader("Upload PDF/CSV", type=["pdf", "csv"])
        if uploaded:
            st.success("📨 Received! Your request has been assigned to expert #TAX3214. Expect feedback within 48 hours.")

# --- Student Tab ---
with tabs[1]:
    st.header("🎓 Student Tax Assistant")
    st.info("""
As a student in the Netherlands, you might be eligible for tax refunds if:
- You worked a part-time job and had wage tax withheld.
- You paid tuition fees or health insurance.
- You paid rent and may qualify for housing allowance (huurtoeslag).
""")
    with st.form("student_form"):
        wage_income = st.number_input("Part-time Income (per year)", min_value=0, value=3000)
        tax_withheld = st.number_input("Wage Tax Already Withheld", min_value=0, value=300)
        tuition_paid = st.number_input("Tuition Paid (per year)", min_value=0, value=2200)
        rent_paid = st.number_input("Monthly Rent", min_value=0, value=500)

        submitted = st.form_submit_button("Check Eligibility")
        if submitted:
            refund = tax_withheld
            st.success(f"🎉 You might be eligible for a refund of approx. €{refund:.2f}")

# --- Employee Tab ---
with tabs[2]:
    st.header("👔 Employee Tax Check")
    st.info("""
You are an employee if:
- You receive monthly salary from one or more employers.
- You receive payslips and tax is withheld (loonheffing).
- You may have extra costs like commuting or dual residency.
""")
    with st.form("employee_form"):
        total_income = st.number_input("Annual Gross Salary", min_value=0, value=32000)
        tax_withheld = st.number_input("Total Wage Tax Withheld", min_value=0, value=9000)
        other_income = st.number_input("Side Income (if any)", min_value=0, value=0)
        commuting_cost = st.number_input("Annual Commuting Cost", min_value=0, value=1200)

        submitted = st.form_submit_button("Estimate Tax Position")
        if submitted:
            est_tax = total_income * 0.37
            diff = tax_withheld - est_tax
            if diff > 0:
                st.success(f"🎉 You might be eligible for a refund of approx. €{diff:.2f}")
            else:
                st.warning(f"You may need to pay an additional €{abs(diff):.2f} in taxes.")

# --- Company Tab ---
with tabs[3]:
    st.header("🏢 TaxMate for Employers and Institutions")
    st.markdown("""
Do you manage a team with many **international employees or students**?

TaxMate helps your people file Dutch taxes with ease.  
You can integrate our tool into your **HR, onboarding, or student support workflows**.

### 🔹 Key Features:
- Branded self-service tax assistant portal
- Dedicated dashboard to track usage and results
- Batch access and secure group management
- Optional tax consultant hotline (B2B support)

📩 **Contact us at [team@taxmate.ai](mailto:team@taxmate.ai) to get early access and pricing.**
""")

# Load AI chat component (HTML floating widget)
with open("modules/ai_chat_component.html", "r") as f:
    components.html(f.read(), height=350)
