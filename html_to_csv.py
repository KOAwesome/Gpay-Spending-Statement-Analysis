from bs4 import BeautifulSoup
import pandas as pd


def extract_gpay_transactions(html_path):
    with open(html_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    transactions = []  # Initialize an empty list to store transactions

    # Find all transaction divs
    for cell in soup.find_all("div", class_="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1"):
        text = cell.get_text(separator=" ").strip()  # Ensure correct spacing
            
        transactions.append(text)

    # Convert to DataFrame
    df = pd.DataFrame(transactions, columns=["text"])

    # # Convert only valid dates, replace invalid ones with NaT
    # df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    return df


df_gpay = extract_gpay_transactions("gpay_statement.html")
print(df_gpay.head(15))
