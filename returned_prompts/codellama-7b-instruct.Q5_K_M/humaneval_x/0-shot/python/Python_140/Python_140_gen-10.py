
def fix_spaces(text):
    # Replace spaces with underscores
    text = text.replace(' ', '_')
    # Replace consecutive spaces with -
    text = text.replace('__', '-')
    return text
