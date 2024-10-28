def text_match_three(text):
    return text.startswith("abbb") and text[3] != "a"

# Test
assert not text_match_three("ac")
assert text_match_three("abbb") == True
assert text_match_three("abbbac") == False
assert text_match_three("abbbabbb") == True
assert text_match_three("abbbab") == False
assert text_match_three("ab") == False
assert text_match_three("abb") == False
assert text_match_three("abbbac") == False
assert text_match_three("abbbabbb") == True
assert text_match_three("abbbab") == False
assert text_match_three("a") == False
assert text_match_three("abc") == False
assert text_match_three("abb") == False
assert text_match_three("abbba") == False
assert text_match_three("abbbaa") == False
assert text_match_three("abbbaaa") == False
assert text_match_three("abbb") == False
assert text_match_three("abbbb") == False
assert text_match_three("abbbb") == False
assert text_match_three("abbbbb") == False
assert text_match_three("abbbbbb") == False
assert text_match_three("abbbbbbb") == False
assert text_match_three("abbbbbbbb") == False
assert text_match_three("abbbbbbbbb") == False
assert text_match_three("abbbbbbbbbb") == False
assert text_match_three("abbbbbbbbbbb") == False
assert text_match_three("abbbbbbbbbbbb") == False
assert text_match_three("abbbbbbbbbbbbb") == False
assert text_match_three("abbbbbbbbbbbbbb") == False
assert text_match_three("abbbbbbbbbbbbbbb") == False
assert text_match_three("abbbbbbbbbbbbbbbb") == False
assert text_match_three("abbbbbbbbbbbbbbbbbb") == False
assert text_match_three("abbbbbbbbbbbbbbbbb") == False
assert text_match_three("abbbbbbbbbbbbbbbbbb") == False
assert text_match_three("abbbbbbbbbbbbbbbbbbb") == False
assert text_match_three("abbbbbbbbbbbbbbbbbbbb") == False
assert text_match_three("abbbbbbbbbbbbbbbbbbbbbb") == False
assert text_match_three("abbbbbbbbbbbbbbbbbbbbb") == False
assert text_match_three("abbbbbbbbbbbbbbbbbbbbbb") == False
