def load_template(path="templates/email_template.txt"):
    """Read and return the raw template text."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def render_template(template_str, data: dict):
    """
    Replace {{placeholders}} in the template with values from the Excel row.
    Missing values become empty strings.
    """
    output = template_str

    for key, value in data.items():
        placeholder = f"{{{{{key}}}}}"  # produces {{company}}, {{address}}, etc.
        output = output.replace(placeholder, str(value) if value is not None else "")

    return output
