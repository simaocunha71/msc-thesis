"""
def text_match_three(s):
    return 'a' in s and s.replace('b', '', 3) == ''
"""

text_match_three = lambda s: 'a' in s and s.replace('b', '', 3) == ''

# assert not text_match_three("ac")

# assert text_match_three("aba")

# assert text_match_three("abbb")

# assert text_match_three("aabbb")

# assert not text_match_three("abab")

# assert not text_match_three("abbbc")

# assert not text_match_three("aaabbb")

# assert text_match_three("abbbaaabbb")

# assert text_match_three("abbbaaabbba")

# assert text_match_three("abbbaaabbbaa")

# assert not text_match_three("abbbaaabbbaa")

# assert not text_match_three("abbbaaabbbaaa")

# assert not text_match_three("abbbaaabbbaaaa")

# assert not text_match_three("abbbaaabbbaaaax")

# assert text_match_three("abbbaaabbaaaax")

# assert text_match_three("abbbaaabbaaxaa")

# assert text_match_three("abbbaaabbaaxaa")

# assert text_match_three("abbbaaabbaaxax")

# assert text_match_three("abbbaaabbaaxax")

# assert text_match_three("abbbaaabbaaxax")

# assert text_match_three("abbbaaabbaaxax")

# assert text_match_three("abbbaaabbaaxax")

# assert text_match_three("abbbaaabbaaxax")

# assert text_match_three("abbbaaabbaaxax")

# assert text_match_three("abbbaaabbaaxax")

# assert text_match_three("abbbaaabbaaxax")

# assert text_match_three("ab