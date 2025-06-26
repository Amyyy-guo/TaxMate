
def estimate_tax(inputs):
    income = inputs["income"]
    vat = inputs["vat_collected"]
    deductions = []

    base_tax_rate = 0.37
    deduction_amount = 0

    if inputs["home_office"]:
        deductions.append("🏠 Home Office Deduction")
        deduction_amount += 1000

    if inputs["health_insurance"]:
        deductions.append("🩺 Health Insurance Deduction")
        deduction_amount += 800

    if inputs["education"]:
        deductions.append("📚 Education Cost Deduction")
        deduction_amount += 1200

    taxable_income = max(income - deduction_amount, 0)
    tax = taxable_income * base_tax_rate
    vat_payable = vat * 0.7

    return {
        "income_tax": round(tax, 2),
        "vat": round(vat_payable, 2),
        "deductions": deductions
    }
