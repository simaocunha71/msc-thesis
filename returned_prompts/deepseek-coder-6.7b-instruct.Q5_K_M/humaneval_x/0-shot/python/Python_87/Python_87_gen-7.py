
def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        for j, num in enumerate(row):
            if num == x:
                coordinates.append((i, j))
    return sorted(coordinates, key=lambda x: (x[0], -x[1]))


# Test cases
print(get_row([[1,2,3,4,5,6],[1,2,3,4,1,6],[1,2,3,4,5,1]], 1))  # [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
print(get_row([], 1))  # []
print(get_row([[], [1], [1, 2, 3]], 3))  # [(2, 2)]
print(get_row([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 3))  # [(2, 0)]
print(get_row([[1, 1, 1], [1, 1, 2], [1, 1, 3]], 1))  # [(0, 0), (1, 0), (2, 0)]
print(get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5))  # [(1, 1)]

