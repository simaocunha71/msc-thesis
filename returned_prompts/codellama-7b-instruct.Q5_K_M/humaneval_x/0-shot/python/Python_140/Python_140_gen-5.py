
def fix_spaces(text):
    if text == '':
        return text
    else:
        if text.count(' ') == 1:
            return text.replace(' ', '_')
        else:
            return text.replace(' ', '-')
