# 📧 Email Automation Tool (Python + Gmail API)

This project is a lightweight and customizable **email automation tool** that reads contact information from an Excel file and sends personalized emails using the **Gmail API (OAuth2)**. 

It is designed for freelancers, small businesses, and anyone who needs to send automated, personalized outreach messages.

---

## 🚀 Features

- Read contacts from Excel (`.xlsx`)
- Gmail authentication via OAuth2 (secure)
- Personalized email templates (`{{company}}`, `{{address}}`, etc.)
- Prevents duplicate sends using `sent_log.csv`
- Clean modular codebase
- Easily customizable for clients
- Includes sample template + sample Excel file

---

## 📁 Project Structure

```
EMAIL_AUTOMATION_TOOL/
│
├── src/
│   ├── send_emails.py          # Main runner script
│   ├── gmail_service.py        # Gmail API OAuth + send logic
│   ├── excel_reader.py         # Reads Excel file -> dictionaries
│   ├── template_engine.py      # Renders {{placeholders}} in emails
│
├── templates/
│   └── email_template.txt      # Editable message template
│
├── data/
│   └── sample_contacts.xlsx    # Example input file
│
├── tests/
│   ├── test_excel.py
│   └── test_template.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/email-automation-tool.git
cd email-automation-tool
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Gmail API Setup

1. Go to **Google Cloud Console**
2. Create a project
3. Enable **Gmail API**
4. Create OAuth credentials:
   - Type: **Desktop App**
5. Download `credentials.json`
6. Place it in the project root (same level as `README.md`)

> ⚠️ Do **NOT** upload `credentials.json` or `token.json` to GitHub.

First-time running will open a browser window to authenticate.

---

## ▶️ Running the Tool

Place your Excel file in `/data`, then run:

```bash
python src/send_emails.py
```

Output will show:
- Loaded contacts  
- Skipped duplicates  
- Successfully sent messages  
- Any errors  

The script automatically creates:

- `token.json` — OAuth refresh token  
- `sent_log.csv` — list of emails already processed  

---

## 📝 Email Template Usage

Edit `/templates/email_template.txt`:

```
Hi {{company}},

I noticed your business at {{address}} and wanted to reach out.

Best regards,
Jem
```

Every column in your Excel sheet becomes a `{{placeholder}}`.

---

## 📊 Excel Input Format

Your file must contain an **Email** column, plus any additional fields you want to use in templates:

Example:

| company        | email              | address        | phone     |
|----------------|--------------------|----------------|-----------|
| Star Auto Ltd  | info@starauto.com  | 123 Dallas Rd  | 555-1234  |

---

## ⚠️ Important Notes

- Never upload real customer data  
- Never upload OAuth credentials  
- Use only the included sample file in GitHub  

---

## 📄 License

MIT License

---

## 👤 Author

Jem Geronimo  
Tech VA & Automation Developer

