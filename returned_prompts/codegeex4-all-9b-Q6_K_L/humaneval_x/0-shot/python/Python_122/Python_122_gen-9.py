def add_elements(arr, k):
    return sum(int(x) for x in arr[:k] if len(str(x)) <= 2)

# Test cases
assert add_elements([111,21,3,4000,5,6,7,8,9], 4) == 24
assert add_elements([1,2,3,4,5,6,7,8,9], 9) == 45
assert add_elements([1,2,3,4,5,6,7,8,9], 1) == 1
assert add_elements([1,2,3,4,5,6,7,8,9], 0) == 0
assert add_elements([], 0) == 0