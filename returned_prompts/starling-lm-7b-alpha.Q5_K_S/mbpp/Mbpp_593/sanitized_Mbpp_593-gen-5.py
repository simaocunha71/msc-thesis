def removezero_ip(str):
    if str[0]=='0':
        return removezero_ip(str[1:])
    else:
        return str