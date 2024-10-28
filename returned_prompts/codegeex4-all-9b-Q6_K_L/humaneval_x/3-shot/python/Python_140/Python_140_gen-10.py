    text = text.replace(' ', '_')

    while '__' in text:
        text = text.replace('__', '-')

    return text

