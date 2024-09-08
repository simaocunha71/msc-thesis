def text_starta_endb(txt):
    if re.fullmatch(r'a.*b$', txt):
        return True
    else:
        return False