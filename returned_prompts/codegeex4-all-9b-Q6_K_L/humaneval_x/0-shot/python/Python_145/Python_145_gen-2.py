def order_by_points(nums):
    def sum_digits(n):
        return sum(int(digit) for digit in str(abs(n)))

    return sorted(nums, key=sum_digits)

print(order_by_points([1, 11, -1, -11, -12]))  # [-1, -11, 1, -12, 11]
print(order_by_points([]))  # []