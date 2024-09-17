def text_match_wordz_middle(string):
    # return True if 'z' is present in the string and not at the start or end
    # else return False
    if 'z' in string:
        if string[0] != 'z' and string[-1] != 'z':
            return True
    return False