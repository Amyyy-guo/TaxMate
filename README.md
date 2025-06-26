
# 🇳🇱 TaxMate - Smart Dutch Tax Assistant

**TaxMate** is a user-friendly web tool that helps freelancers, students, and employees in the Netherlands understand their tax obligations, estimate their tax returns, and simplify interactions with the tax system.

> Created as part of the MSc Business Analytics Management FinTech project  
> Author: **Yuqing Guo**

---

## 🚀 Key Features

- 🔐 **Simulated connection to Belastingdienst** (DigiD / Mijn Belastingdienst)
- 📊 **Tax estimation** for Freelancers (ZZP), Students, and Employees
- 📤 **Expert review module**: upload documents for human expert check
- 🤖 **AI Chat Assistant** in floating window (RAG simulation)
- 📥 **Downloadable tax report** in CSV format
- 🏢 **B2B support page** for employers and institutions

---

## 👥 Target Users

| User Type     | Features |
|---------------|----------|
| **Freelancer / ZZP** | Input income, deductions, VAT collected. See estimated income tax and VAT due. |
| **Student**   | Estimate refund based on part-time income, tuition, rent. |
| **Employee**  | Enter salary and costs to estimate refund or payment due. |
| **Companies / Orgs** | Learn about B2B integration for international teams. |

---

## ⚙️ Tech Stack

- **Python 3.10+**
- **Streamlit** (main UI framework)
- `pandas`, `datetime`, `io` (data handling)
- **HTML/CSS** embedded component (for AI assistant)
- Modular architecture with:
  - `input_forms.py` – dynamic forms
  - `tax_logic.py` – business logic
  - `export_utils.py` – CSV exports

---

## 📸 Screenshots

> 💼 ZZP Form Example  
> 🎓 Student Refund Estimator  
> 🔐 Simulated Belastingdienst Login  
> 🤖 Floating AI Chat Assistant  
> 📤 Document Upload for Expert Review
https://github.com/Amyyy-guo/TaxMate/blob/fb4e3e4316e4bccc436d5c37fe8bf57379fe4883/Income.png
---

## 🧪 How to Run Locally

1. Clone or download this repo
2. Make sure you have Python 3.10+ installed
3. Install dependencies:

```bash
pip install streamlit pandas
```

4. Run the app:

```bash
streamlit run app.py
```

---

## 🌱 Future Improvements

- 🔗 Real integration with Belastingdienst via APIs
- 🧠 Real Retrieval-Augmented Generation (RAG) AI model using GPT + vector DB
- 👩‍💼 Expert review portal with dashboard and ticket tracking
- 🧾 Monthly bookkeeping assistant for freelancers
- 🌐 Deploy to Streamlit Cloud or custom domain

---

## 👩‍💻 Author

**Yuqing Guo**  
MSc Business Analytics Management  
Email:607267yg@eur.nl


---
