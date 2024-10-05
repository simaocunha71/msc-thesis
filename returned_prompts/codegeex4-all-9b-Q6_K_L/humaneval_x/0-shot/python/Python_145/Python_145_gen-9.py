def order_by_points(nums):
    return sorted(nums, key=lambda x: sum(map(int, str(x))))

print(order_by_points([1, 11, -1, -11, -12]))
print(order_by_points([]))