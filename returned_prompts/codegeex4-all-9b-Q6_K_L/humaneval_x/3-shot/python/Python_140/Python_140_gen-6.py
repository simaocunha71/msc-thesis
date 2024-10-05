    import re

    text = re.sub(' +', '-', text)
    text = re.sub(' ', '_', text)

    return text

