def sequence(n):
    if n==0:
        return 2
    elif n==1:
        return 3
    elif n==2:
        return 5
    elif n==3:
        return 8
    elif n==4:
        return 13
    elif n>4:
        return sequence(n-1)+sequence(n-2)+sequence(n-3)
    else:
        return 0