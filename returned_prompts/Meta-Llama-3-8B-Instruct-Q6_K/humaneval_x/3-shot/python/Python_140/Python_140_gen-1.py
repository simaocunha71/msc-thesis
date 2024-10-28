    text = text.replace(" ", "_")
    while "--" in text:
        text = text.replace("--", "-")
    return text


