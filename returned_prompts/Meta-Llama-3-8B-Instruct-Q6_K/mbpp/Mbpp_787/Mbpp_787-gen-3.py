def text_match_three(text):
    if len(text) < 4:
        return False
    if text[0] != 'a':
        return False
    if text[1:4] != 'bbb':
        return False
    return True
assert not text_match_three("ac")
assert text_match_three("abbb") == True
assert text_match_three("abb") == False
assert text_match_three("abbbb") == False
assert text_match_three("a") == False
assert text_match_three("aabb") == False
assert text_match_three("abbbbc") == True
assert text_match_three("abbbbd") == False
assert text_match_three("abbba") == False
assert text_match_three("abbb") == False
assert text_match_three("abc") == False
assert text_match_three("abbbca") == True
assert text_match_three("abbbcb") == False
assert text_match_three("abbbcca") == False
assert text_match_three("abbbcc") == False
assert text_match_three("abbbccaa") == True
assert text_match_three("abbbccab") == False
assert text_match_three("abbbccac") == False
assert text_match_three("abbbcc") == False
assert text_match_three("abbbccc") == False
assert text_match_three("abbbcccbb") == True
assert text_match_three("abbbcccba") == False
assert text_match_three("abbbcccbb") == True
assert text_match_three("abbbcccbbb") == True
assert text_match_three("abbbcccbb") == True
assert text_match_three("abbbcccbbbb") == True
assert text_match_three("abbbcccbbbbbb") == True
assert text_match_three("abbbcccbbbbbbb") == True
assert text_match_three("abbbcccbbbbbbbbb") == True
assert text_match_three("abbbcccbbbbbbbbbb") == True
assert text_match_three("abbbcccbbbbbbbbbbb") == True
assert text_match_three("abbbcccbbbbbbbbbbbbb") == True
assert text_match_three("abbbcccbbbbbbbbbbbbb") == True
assert text_match_three("abbbcccbbbbbbbbbbbbbbb") == True
assert text_match_three("abbbcccbbbbbbbbbbbbbbb") == True
assert text_match_three("abbbcccbbbbbbbbbbbbbbb")