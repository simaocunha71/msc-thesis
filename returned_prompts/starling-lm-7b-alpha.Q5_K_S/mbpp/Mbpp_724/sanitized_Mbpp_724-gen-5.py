def power_base_sum(base,power):
    sums=0
    for i in range(power+1):
        sums+=base**i
    return sums