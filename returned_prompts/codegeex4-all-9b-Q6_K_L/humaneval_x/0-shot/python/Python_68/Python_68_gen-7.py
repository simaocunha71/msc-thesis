def pluck(arr):
    smallest_even = float('inf')
    smallest_even_index = -1
    for i, value in enumerate(arr):
        if value % 2 == 0 and value < smallest_even:
            smallest_even = value
            smallest_even_index = i
    return [smallest_even, smallest_even_index] if smallest_even_index != -1 else []

print(pluck([4,2,3])) # [2, 1]
print(pluck([1,2,3])) # [2, 1]
print(pluck([])) # []
print(pluck([5, 0, 3, 0, 4, 2])) # [0, 1]