    text = text.replace(" ", "_")
    while True:
        text = text.replace("___", "-")
        if text.count("_") <= 2:
            break
    return text


