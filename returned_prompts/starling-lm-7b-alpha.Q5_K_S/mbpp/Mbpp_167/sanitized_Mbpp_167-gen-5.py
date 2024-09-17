def next_power_of_2(n):
    if(n==0):
        return 1
    i=1
    while(i<n):
        i=i*2
    return i