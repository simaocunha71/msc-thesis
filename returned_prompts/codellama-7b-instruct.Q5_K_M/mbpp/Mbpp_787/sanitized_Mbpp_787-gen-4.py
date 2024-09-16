def text_match_three(string):
    # Find all matches of 'a' followed by 3 'b' in a string
    pattern = r"a[b]{3}"
    return re.search(pattern, string) != None