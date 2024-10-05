def add_elements(arr, k):
    total = 0
    for num in arr[:k]:
        if num < 10:
            total += num
        elif num < 100:
            total += num
    return total

print(add_elements([111,21,3,4000,5,6,7,8,9], 4)) # Output: 24