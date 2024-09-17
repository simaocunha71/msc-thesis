def next_power_of_2(n):
    if(n == 0):
        return 1
    else:
        if(n & (n - 1) == 0):
            return n
        else:
            return 2 * next_power_of_2(n & (n - 1))