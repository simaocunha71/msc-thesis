"""
def sum_even_and_even_index(numbers):
    result = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0 and i % 2 == 0:
            result += numbers[i]
    return result

print(sum_even_and_even_index([5, 6, 12, 1, 18, 8]))
"""

def sum_even_and_even_index(numbers):
    result = 0
    for i in range(len(numbers)):
        if i % 2 == 0 and numbers[i] % 2 == 0:
            result += numbers[i]
    return result

print(sum_even_and_even_index([5, 6, 12, 1, 18, 8]))


# Made By Mostafa_Khaled
```