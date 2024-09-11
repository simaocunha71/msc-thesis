def text_starta_endb(s):
    return s.startswith("a") and s.endswith("b") and "a" in s and "b" in s and s.count("a") == 1 and s.count("b") == 1