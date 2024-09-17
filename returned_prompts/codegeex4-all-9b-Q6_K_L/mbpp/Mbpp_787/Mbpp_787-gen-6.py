def text_match_three(s):
    match = re.fullmatch(r'a.*?b.*?b.*?b', s)
    return bool(match)