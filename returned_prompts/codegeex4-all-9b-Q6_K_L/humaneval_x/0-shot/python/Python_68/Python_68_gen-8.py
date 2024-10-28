def pluck(arr):
    smallest_even = float('inf')
    smallest_index = float('inf')
    for i, num in enumerate(arr):
        if num % 2 == 0 and num < smallest_even:
            smallest_even = num
            smallest_index = i
    if smallest_even == float('inf'):
        return []
    return [smallest_even, smallest_index]

print(pluck([4,2,3]))
print(pluck([1,2,3]))
print(pluck([]))
print(pluck([5, 0, 3, 0, 4, 2]))