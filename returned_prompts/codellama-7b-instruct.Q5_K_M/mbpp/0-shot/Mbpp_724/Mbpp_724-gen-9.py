def power_base_sum(base,power):
    sum_of_digits=0
    for i in range(power):
        sum_of_digits+=int(base)
        base*=10
    return sum_of_digits



