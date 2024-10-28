def power_base_sum(base, power):
    # return sum(map(int, str(base)**power))
    return sum(int(i) for i in str(base**power))