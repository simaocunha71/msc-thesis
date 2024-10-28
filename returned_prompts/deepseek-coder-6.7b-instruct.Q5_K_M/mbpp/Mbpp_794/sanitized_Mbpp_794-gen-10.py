def text_starta_endb(text):
    pattern = re.compile(r'a.*b$')
    if pattern.match(text):
        return True
    else:
        return False