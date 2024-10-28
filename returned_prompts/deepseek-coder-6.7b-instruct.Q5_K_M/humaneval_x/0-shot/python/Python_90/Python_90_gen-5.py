
def next_smallest(lst):
    if len(lst) < 2:
        return None

    min1 = min2 = float('inf')
    for x in lst:
        if x <= min1:
            min1, min2 = x, min1
        elif x < min2:
            min2 = x

    return min2 if min2 < float('inf') else None

print(next_smallest([1, 2, 3, 4, 5])) # 2
print(next_smallest([5, 1, 4, 3, 2])) # 2
print(next_smallest([])) # None
print(next_smallest([1, 1])) # None

Explanation:
The function works by keeping track of the smallest and second smallest elements in the list. It iterates through the list and updates these values whenever it finds a smaller or second smaller number. Finally, it returns the second smallest number. If there is no second smallest number, it returns None.
"""

# Test cases:
print(next_smallest([1, 2, 3, 4, 5])) # 2
print(next_smallest([5, 1, 4, 3, 2])) # 2
print(next_smallest([])) # None
print(next_smallest([1, 1])) # None
print(next_smallest([10, 20, 10, 40, 50])) # 20
print(next_smallest([10, 20, 30, 50, 40])) # 20
print(next_smallest([10, 10, 10, 10, 10])) # None
print(next_smallest([-10, -20, -30, -50, -40])) # -20
print(next_smallest([100, 200, 300, 400, 500])) # 200
print(next_smallest([100, 200, 100, 400, 