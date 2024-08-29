def text_match_wordz_middle(text):
    import re
    return bool(re.search(r'z[^z]*z', text))

# Test the function
print(text_exact_match("pythonzabc.")) # should return True

