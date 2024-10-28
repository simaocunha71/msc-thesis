def text_match_two_three(s):
    match = re.match(r'a(b{2,3})', s)
    return bool(match)