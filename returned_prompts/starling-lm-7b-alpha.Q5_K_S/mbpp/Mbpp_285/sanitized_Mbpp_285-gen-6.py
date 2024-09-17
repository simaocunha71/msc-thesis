def text_match_two_three(string):
    if len(string)<3:
        return False
    if string[0]=='a' and string[1]=='b' and string[2]=='b':
        return True
    if string[0]=='a' and string[1]=='b' and string[2]=='c':
        return True
    else:
        return False