    return sum(lst[i]**2 if i%3==0 else (lst[i]**3 if i%4==0 else lst[i]) for i in range(len(lbuf)))


