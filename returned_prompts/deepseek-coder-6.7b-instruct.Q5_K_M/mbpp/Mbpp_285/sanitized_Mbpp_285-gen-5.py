def text_match_two_three(text):
    pattern = re.compile(r'ab{2,3}')
    if pattern.search(text):
        return True
    else:
        return False