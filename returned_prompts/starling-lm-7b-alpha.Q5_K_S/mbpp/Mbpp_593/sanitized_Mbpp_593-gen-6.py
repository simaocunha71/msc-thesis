def removezero_ip(ip):
    ip=list(ip)
    for i in range(len(ip)):
        if ip[i]=='0':
            del ip[i]
            i-=1
    ip=''.join(ip)
    return ip