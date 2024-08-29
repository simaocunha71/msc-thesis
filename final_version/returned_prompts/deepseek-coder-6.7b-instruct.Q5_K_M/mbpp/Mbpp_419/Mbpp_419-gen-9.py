
def round_and_sum(nums):
    rounded = [round(n) for n in nums]
    return sum(rounded) * len(rounded)

print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])) # 243


"""
