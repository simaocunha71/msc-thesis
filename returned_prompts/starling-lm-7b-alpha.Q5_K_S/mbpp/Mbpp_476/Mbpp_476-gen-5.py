def big_sum(numbers):
    return sum(numbers) - min(numbers) + max(numbers)


# Testing
print(big_sum([1, 2, 3]))  # Should print: 4
print(big_sum([-3, 4, 7]))  # Should print: 10
print(big_sum([10, 10, 10]))  # Should print: 30
print(big_sum([1, 2, 3, 4]))  # Should print: 6


# Testing with negative numbers and zero
print(big_sum([-3, -4, 7]))  # Should print: 4
print(big_sum([-3, 4, -7]))  # Should print: 0
print(big_sum([-3, 4, 0]))  # Should print: 1
print(big_sum([0, 4, 7]))  # Should print: 11
print(big_sum([-3, 0, 7]))  # Should print: 10
print(big_sum([-3, 0, 0]))  # Should print: 0


# Testing with one number
print(big_sum([-3]))  # Should print: -3
print(big_sum([0]))  # Should print: 0
print(big_sum([3]))  # Should print: 3
print(big_sum([-3]))  # Should print: -3
print(big_sum([4]))  # Should print: 4
print(big_sum([7]))  # Should print: 7


# Testing with zero numbers
print(big_sum([]))  # Should print: 0
print(big_sum([0]))  # Should print: 0
print(big_sum([0, 0]))  # Should print: 0
print(big_sum([0, 0, 0]))  # Should print: 0
print(big_sum([0, 0, 0, 0]))  # Should print: 0
print(big_sum([0, 0, 0, 0,