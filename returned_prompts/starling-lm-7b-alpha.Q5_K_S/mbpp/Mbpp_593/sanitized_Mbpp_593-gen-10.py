def removezero_ip(s):
    while s[0]=='0' and len(s)>1:
        s=s[1:]
    while s[-1]=='0' and len(s)>3:
        s=s[:-1]
    return s