from template_engine import load_template, render_template

dummy_data = {
    "company": "TestCorp",
    "address": "100 Main St",
    "email": "test@example.com"
}

template = load_template()
result = render_template(template, dummy_data)

print(result)
