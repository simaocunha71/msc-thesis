def text_match_two_three(my_string):
    pattern = r"a[b]{2,3}"
    if re.search(pattern, my_string):
        return True
    return False

