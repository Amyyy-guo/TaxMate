
import streamlit as st

def get_user_inputs(role="zzp"):
    st.markdown("### 📈 Income Information")
    income = st.number_input("Total Income (per year)", min_value=0, value=40000)
    vat_collected = st.number_input("Total VAT Collected (per year)", min_value=0, value=5000)
    st.caption("💡 Usually 21% VAT is added to invoices. This is the total VAT collected from clients.")

    st.markdown("### 💼 Business Costs & Deductions")
    use_home_office = st.checkbox("🏠 I use my home as an office")
    health_insurance = st.checkbox("🩺 I pay for Dutch health insurance")
    self_education = st.checkbox("📚 I paid for relevant self-education or training")

    return {
        "income": income,
        "vat_collected": vat_collected,
        "home_office": use_home_office,
        "health_insurance": health_insurance,
        "education": self_education
    }
