def text_starta_endb(s):
    match = re.search(r'a.*b$', s)
    if match:
        return True
    else:
        return False