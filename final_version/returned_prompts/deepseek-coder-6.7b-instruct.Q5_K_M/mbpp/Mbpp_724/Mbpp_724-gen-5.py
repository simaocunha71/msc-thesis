def power_base_sum(base, power):
    num = base**power
    return sum(int(i) for i in str(num))

print(power_base_sum(10,10))
print(power_base_sum(8,8))

