"""
def power_base_sum(base, power):
    if power == 0:
        return 0
    elif power == 1:
        return base
    else:
        return base + power_base_sum(base, power-1)

print(power_base_sum(2,100)) #115
"""

