def next_power_of_2(n):
    if n==0:
        return 1
    else:
        while n%2!=1:
            n = n*2
    return n