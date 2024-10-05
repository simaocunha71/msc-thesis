def order_by_points(nums):
    def key(n):
        return sum(int(d) for d in str(abs(n)))
    return sorted(nums, key=key)

print(order_by_points([1, 11, -1, -11, -12]))  # [-1, -11, 1, -12, 11]
print(order_by_points([]))  # []
print(order_by_points([1, 11, 0, -11, 12]))  # [0, 1, -11, 11, 12]