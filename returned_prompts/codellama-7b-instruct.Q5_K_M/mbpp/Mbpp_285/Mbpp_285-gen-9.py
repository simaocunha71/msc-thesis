def text_match_two_three(text):
    return bool(re.match(r"a[b]{2,3}", text))


