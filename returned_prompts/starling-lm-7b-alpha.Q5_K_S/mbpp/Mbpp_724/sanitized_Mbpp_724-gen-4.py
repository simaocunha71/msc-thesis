def power_base_sum(base, power):
    ans = 0
    for i in range(power+1):
        ans += pow(base, i, 10)
    return ans