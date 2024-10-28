def text_starta_endb(text):
    return bool(re.match("a.*b$", text))