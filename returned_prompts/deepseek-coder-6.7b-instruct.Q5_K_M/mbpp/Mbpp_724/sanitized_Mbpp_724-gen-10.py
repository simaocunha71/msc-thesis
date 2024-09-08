def power_base_sum(base, power):
    num = base**power
    return sum(int(i) for i in str(num))