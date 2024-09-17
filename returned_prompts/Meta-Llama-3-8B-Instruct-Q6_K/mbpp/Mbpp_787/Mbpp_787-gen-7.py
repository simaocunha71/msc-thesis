def text_match_three(text):
    if len(text) >= 4 and text[0] == 'a' and text[1:4] == 'bbb':
        return True
    else:
        return False
assert not text_match_three("ac")
assert not text_match_three("a")
assert not text_match_three("ab")
assert not text_match_three("abb")
assert not text_match_three("abbb")
assert not text_match_three("abbbb")
assert text_match_three("abbbb")
assert text_match_three("abbbbb")
assert text_match_three("abbbbbb")  # this one is very long! 
assert text_match_three("abb")  # this one is not long enough!  # fails! 
assert not text_match_three("abc")  # this one is not even long enough!  # fails! 
assert not text_match_three("abcd")  # this one is not even long enough!  # fails! 
assert not text_match_three("abbbcc")  # this one is long enough, but does not start with 'a'!  # fails! 
assert text_match_three("abbbccc")  # this one is long enough, but does not start with 'a'!  # fails! 
assert not text_match_three("abbbcccddd")  # this one is long enough, but does not start with 'a'!  # fails! 
assert text_match_three("abbbcccdd")  # this one is long enough, but does not start with 'a'!  # fails! 
assert not text_match_three("abbbcccddd")  # this one is long enough, but does not start with 'a'!  # fails! 
assert not text_match_three("abbbcccdd")  # this one is long enough, but does not start with 'a'!  # fails! 
assert not text_match_three("abbbcccddd")  # this one is long enough, but does not start with 'a'!  # fails! 
assert not text_match_three("abbbcccdd")  # this one is long enough, but does not start with 'a'!  # fails! 
assert not text_match_three("abbbcccddd")  # this one is long enough, but does not start with 'a'!  # fails! 
assert not text_match_three("abbbcccdd")  # this one is long enough, but does not start