
    def sum_digits(n):
        if n < 0:
            n = -n
        return sum(int(digit) for digit in str(n))

    return sorted(nums, key=lambda n: (sum_digits(n), nums.index(n)))

print(order_by_points([1, 11, -1, -11, -12]))
print(order_by_points([]))

# ---------
"""
