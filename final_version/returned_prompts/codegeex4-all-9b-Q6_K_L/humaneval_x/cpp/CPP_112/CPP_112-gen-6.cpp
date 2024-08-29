def reverse_delete(s,c):
    for x in c:
        s=s.replace(x,'')
    if s==s[::-1]:
        return [s,'True']
    else:
        return [s,'False']
