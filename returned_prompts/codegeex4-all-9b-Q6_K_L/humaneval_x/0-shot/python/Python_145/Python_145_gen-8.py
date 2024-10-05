def order_by_points(nums):
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))

    return sorted(nums, key=digit_sum)

print(order_by_points([1, 11, -1, -11, -12]))  # [-1, -11, 1, -12, 11]
print(order_by_points([]))  # []