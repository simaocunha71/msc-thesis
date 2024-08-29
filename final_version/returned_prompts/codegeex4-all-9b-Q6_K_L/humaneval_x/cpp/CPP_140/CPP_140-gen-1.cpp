def fix_spaces(text):
    text = text.replace(' ', '_')
    while '__' in text:
        text = text.replace('__', '_')
    return text.replace('_ ', '-')

B:
def fix_spaces(text):
    text = text.replace('  ', '-')
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text.replace(' ', '_')

C:
def fix_spaces(text):
    text = text.replace(' ', '_')
    while '  ' in text:
        text = text.replace('  ', '-')
    return text.replace(' ', '_')

D:
def fix_spaces(text):
    text = text.replace(' ', '_')
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text.replace(' ', '-')

E:
def fix_spaces(text):
    text = text.replace(' ', '_')
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text.replace(' ', '_')