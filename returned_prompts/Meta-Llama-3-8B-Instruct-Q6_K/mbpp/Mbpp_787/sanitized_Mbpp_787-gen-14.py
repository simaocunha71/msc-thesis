def text_match_three(text):
    return "ab" in text and text.count("ab") == 1 and "abb" in text and text.count("abb") == 1 and "abbb" in text and text.count("abbb") == 1