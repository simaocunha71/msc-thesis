def text_match_wordz_middle(text):
    import re
    pattern = r"^[^z]*z[^z]*$"
    if re.search(pattern, text):
        return True
    else:
        return False

print(text_match_wordz_middle("pythonzabc."))


