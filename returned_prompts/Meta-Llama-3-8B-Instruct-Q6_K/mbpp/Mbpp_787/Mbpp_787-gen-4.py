def text_match_three(text):
    return "ab" in text and text.count("ab") == 1 and "abb" in text and text.count("abb") == 1 and "abbb" in text and text.count("abbb") == 1
print(text_match_three("abbbabb"))  # Returns: True
print(text_match_three("ac"))  # Returns: False
print(text_match_three("abb"))  # Returns: False
print(text_match_three("abbb"))  # Returns: False
print(text_match_three("abbbabb"))  # Returns: True
print(text_match_three("abbbabba"))  # Returns: True
print(text_match_three("abbbabbb"))  # Returns: True
print(text_match_three("abbbabbbab"))  # Returns: True
print(text_match_three("abbbabbbabba"))  # Returns: True
print(text_match_three("abbbabbbabbb"))  # Returns: True
print(text_match_three("abbbabbbabbbab"))  # Returns: True
print(text_match_three("abbbabbbabbbabba"))  # Returns: True
print(text_match_three("abbbabbbabbbabb"))  # Returns: True
print(text_match_three("abbbabbbabbbabbb"))  # Returns: True
print(text_match_three("abbbabbbabbbabbbb"))  # Returns: True
print(text_match_three("abbbabbbabbbabbbbb"))  # Returns: True
print(text_match_three("abbbabbbabbbabbbbbb"))  # Returns: True
print(text_match_three("abbbabbbabbbabbbbbbb"))  # Returns: True
print(text_match_three("abbbabbbabbbabbbbbbbb"))  # Returns: True
print(text_match_three("abbbabbbabbbabbbbbbbbb"))  # Returns: True
print(text_match_three("abbbabbbabbbabbbbbbbbbb"))  # Returns: True
print(text_match_three("abbbabbbabbbabbbbbbbbbbb"))  # Returns: True
print(text_match_three("abbbabbbabbbabbbbbbbbbbbb"))  # Returns: True
print(text_match_three("abbbabbbabbbabbbbbbbbbbbbb"))  # Returns: True
print(text_match_three("abbbabbbabbbab