
    l.sort()
    for i in range(len(l)-2):
        if l[i]==l[i-1]:
            continue
        for j in range(i+1, len(l)-1):
            if l[j]==l[j-1]:
                continue
            for k in range(j+1, len(l)):
                if l[k]==l[k-1]:
                    continue
                if l[i]+l[j]+l[k]==0:
                    return True
    return False