def move_num(s):
    s=list(s)
    s.sort(key=str.isdigit)
    for i in range(len(s)):
        if s[i]=='1' or s[i]=='2' or s[i]=='3' or s[i]=='4' or s[i]=='5' or s[i]=='6' or s[i]=='7' or s[i]=='8' or s[i]=='9' or s[i]=='0':
            s[i]=s[i]+s[len(s)-i-1]
            del(s[len(s)-i-1])
    return (''.join(s))