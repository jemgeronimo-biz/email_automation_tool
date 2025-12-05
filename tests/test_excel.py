from excel_reader import load_contacts

contacts = load_contacts("sample_contacts.xlsx")

for c in contacts[:5]:
    print(c)
