def text_lowercase_underscore(s):
    if s=='':
        return False
    else:
        if s[0]=='_':
            return False
        else:
            if s[-1]=='_':
                return False
            else:
                if s.replace('_','').islower():
                    return True
                else:
                    return False





