    import re
    text = re.sub(' +', '-', text)
    text = text.replace(' ', '_')
    return text


