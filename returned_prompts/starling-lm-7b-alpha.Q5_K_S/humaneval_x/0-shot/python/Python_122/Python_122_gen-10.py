
def add_elements(arr, k):
    total = 0
    for i in range(min(k,len(arr))):
        if len(str(arr[i])) <= 2:
            total += arr[i]
    return total

# Test
print(add_elements([111,21,3,4000,5,6,7,8,9], 4))  # 24
print(add_elements([111,21,3,4000,5,6,7,8,9], 100))  # 24

# Time Complexity: O(n)
# Space Complexity: O(1)



# Time Complexity: O(n*k)
# Space Complexity: O(k)
def add_elements(arr, k):
    return sum(arr[:k] if len(str(num)) <= 2 else 0 for num in arr)

# Test
print(add_elements([111,21,3,4000,5,6,7,8,9], 4))  # 24
print(add_elements([111,21,3,4000,5,6,7,8,9], 100))  # 24

# Time Complexity: O(n)
# Space Complexity: O(k)
def add_elements(arr, k):
    return sum(num for i, num in enumerate(arr[:k]) if len(str(num)) <= 2)

# Test
print(add_elements([111,21,3,4000,5,6,7,8,9], 4))  # 24
print(add_elements([111,21,3,4000,5,6,7,8,9], 100))  # 24

# Time Complexity: O(n)
# Space Complexity: O(k)
def add_elements(arr, k):
    return sum(num for num in arr[:k] if len(str(num)) <= 2)

#