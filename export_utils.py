
import pandas as pd
from io import StringIO

def generate_csv(inputs, results):
    data = {
        "Total Income": [inputs["income"]],
        "VAT Collected": [inputs["vat_collected"]],
        "Estimated Income Tax": [results["income_tax"]],
        "Estimated VAT to Pay": [results["vat"]],
        "Deductions Applied": [", ".join(results["deductions"])]
    }
    df = pd.DataFrame(data)
    csv = StringIO()
    df.to_csv(csv, index=False)
    return csv.getvalue()
