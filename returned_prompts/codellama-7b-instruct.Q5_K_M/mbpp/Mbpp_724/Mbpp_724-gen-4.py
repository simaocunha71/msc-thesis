def power_base_sum(base, power):
    total=0
    for i in str(base**power):
        total+=int(i)
    return total


