def add_elements(arr, k):
    return sum(int(x) for x in arr[:k] if len(str(x)) <= 2)

# Test cases
print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4))  # Output: 24
print(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))  # Output: 15
print(add_elements([10, 20, 30, 40, 50, 60, 70, 80, 90], 3))  # Output: 60
print(add_elements([100, 200, 300, 400, 500, 600, 700, 800, 900], 2))  # Output: 0