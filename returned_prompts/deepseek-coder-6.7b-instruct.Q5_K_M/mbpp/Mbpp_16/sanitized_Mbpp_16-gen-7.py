def text_lowercase_underscore(s):
    for i in range(len(s)-1):
        if s[i].islower() and s[i+1].islower() and s[i+1]=="_":
            return True
    return False