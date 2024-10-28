def below_threshold(l: list, t: int):
    return all(x < t for x in l)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))  # Expected output: False
print(below_threshold([1, 2, 3, 4], 5))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 100))  # Expected output: True
print(below_threshold([10, 10, 10, 10], 100))  # Expected output: False
print(below_threshold([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))  # Expected output: False
print(below_threshold([1, 2, 3, 4, 5, 6, 7, 8, 9], 1))  # Expected output: True
print(below_threshold([1, 2, 3, 4, 5, 6, 7, 8, 9], 0))  # Expected output: True
print(below_threshold([-1, -2, -3, -4], 0))  # Expected output: True
print(below_threshold([-1, -2, -3, -4], -5))  # Expected output: False
print(below_threshold([-1, -2, -3, -4, -5, -6, -7, -8, -9], -10))  # Expected output: True
print(below_threshold([-1, -2, -3, -4, -5, -6, -7, -8, -9], -5))  # Expected output: False
print(below_threshold([-1, -2, -3, -4, -5, -6, -7, -8, -9], 0))  # Expected output: False
print(below_threshold([-1, -2, -3, -4, -5, -6, -7, -8, -9], 1))  # Expected output: False
print(below_threshold([-1, -2, -3, -4, -