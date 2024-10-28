
    def sum_of_digits(n):
        if n < 0:
            return sum_of_digits(-n)
        else:
            return sum(int(digit) for digit in str(n))

    return sorted(nums, key=lambda num: (sum_of_digits(num), nums.index(num)))


if __name__ == "__main__":
    print(order_by_points([1, 11, -1, -11, -12]))  # == [-1, -11, 1, -12, 11]
    print(order_by_points([]))  # == []


"""
Test cases:

order_by_points([1, 11, -1, -11, -12]) ➞ [-1, -11, 1, -12, 11]
order_by_points([15, 7, 12, 10, 2]) ➞ [2, 10, 12, 15, 7]
order_by_points([0]) ➞ [0]
order_by_points([]) ➞ []
"""

# Solution by Mystery Persona

def order_by_points(nums):
    return sorted(nums, key=lambda x: (sum(int(i) for i in str(abs(x))), nums.index(x)))

print(order_by_points([1, 11, -1, -11, -12]))  # == [-1, -11, 1, -12, 11]
print(order_by_points([15, 7, 12, 10, 2]))  # == [2, 10, 12, 15, 7]
print(order_by_points([0]))  # == [0]
print(order_by_points([]))  # == []

"""
Test cases:

order_by_points([1, 11, -1, -11, -12])