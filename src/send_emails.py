import os
import pandas as pd
from gmail_service import get_gmail_service, send_email
from excel_reader import load_contacts
from template_engine import load_template, render_template

LOG_PATH = "sent_log.csv"


def load_sent_log():
    """Load the CSV of previously-sent emails to avoid duplicates."""
    if not os.path.exists(LOG_PATH):
        return set()

    df = pd.read_csv(LOG_PATH)
    return set(df["email"].astype(str).tolist())


def append_to_log(contact):
    """Append successful sends to sent_log.csv."""
    exists = os.path.exists(LOG_PATH)

    df = pd.DataFrame([{
        "email": contact.get("email", ""),
        "company": contact.get("company", ""),
    }])

    # append without rewriting header
    df.to_csv(LOG_PATH, mode="a", header=not exists, index=False)


def main():
    excel_path = "data/sample_contacts.xlsx"  # change if needed

    print("Loading contacts...")
    contacts = load_contacts(excel_path)

    print("Loading email template...")
    template = load_template()

    print("Initializing Gmail API...")
    service = get_gmail_service()

    sent_log = load_sent_log()

    print(f"Found {len(contacts)} contacts, {len(sent_log)} already emailed.")

    for contact in contacts:
        email = str(contact.get("email", "")).strip()

        if email in sent_log:
            print(f"[SKIP] Already sent to {email}")
            continue

        # Render message with template
        message_body = render_template(template, contact)

        try:
            print(f"[SENDING] {email} ...")
            send_email(service, email, subject="Hello from Automation Tool", body_text=message_body)

            append_to_log(contact)
            sent_log.add(email)

            print("[OK] Sent successfully.")

        except Exception as e:
            print(f"[ERROR] Failed to send to {email}: {e}")

    print("Done.")


if __name__ == "__main__":
    main()
