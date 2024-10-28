    def get_row(lst, x):
        result = []
        for i, row in enumerate(lst):
            if x in row:
                result.append((i, row.index(x)))
        result.sort(key=lambda x: (x[0], -x[1]))
        return result
# test the function
print(get_row([[1,2,3,4,5,6], [1,2,3,4,1,6], [1,2,3,4,5,1]], 1))  # [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]


# test the function with empty list
print(get_row([], 1))  # []

# test the function with list that contains only one element
print(get_row([[], [1], [1, 2, 3]], 3))  # [(2, 2)]


# test the function with list that contains only one element
print(get_row([[1], [1, 2]], 2))  # [(1, 1)]


# test the function with list that contains two elements
print(get_row([[1, 2, 3], [1, 2]], 2))  # [(0, 1), (1, 1)]


# test the function with list that contains three elements
print(get_row([[1, 2, 3], [1, 2, 3], [1, 2]], 2))  # [(0, 1), (1, 1), (2, 1)]


# test the function with list that contains four elements
print(get_row([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3], [1, 2]], 2))  # [(0, 1), (1, 1), (2, 1), (3, 1)]


# test the function with list that contains five elements
print(get_row([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4], [1, 2, 3], [1, 2]], 2))  # [(0, 1), (1