def text_match_wordz_middle(string):
    #check if the string contains 'z'
    if 'z' not in string:
        return False
    #check if the first and last character are 'z'
    if string[0] == 'z' or string[-1] == 'z':
        return False
    #if none of the above conditions are met, return true
    return True