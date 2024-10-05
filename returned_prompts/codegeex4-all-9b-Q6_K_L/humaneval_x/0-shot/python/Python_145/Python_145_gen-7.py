def order_by_points(nums):
    return sorted(nums, key=lambda x: (sum(int(digit) for digit in str(abs(x)))), reverse=False)

print(order_by_points([1, 11, -1, -11, -12]))  # [-1, -11, 1, -12, 11]
print(order_by_points([]))  # []