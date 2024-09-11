def text_match_two_three(text):
    return text.find("ab") != -1 and text.find("abb") == -1 and text.find("abbb") == -1