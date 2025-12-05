import pandas as pd

def load_contacts(excel_path: str):
    """
    Load Excel data and return a list of contact dictionaries.
    Skips rows without an email address.
    """
    df = pd.read_excel(excel_path)

    # Standardize column names (lowercase, remove spaces)
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    required_columns = ["company", "email"]

    # Warn if required columns are missing
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    contacts = []

    for _, row in df.iterrows():
        if pd.isna(row["email"]):
            continue  # skip rows with no email

        contact_data = row.to_dict()
        contacts.append(contact_data)

    return contacts
