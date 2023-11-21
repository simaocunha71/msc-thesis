
def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    
    lst = sorted(lst)
    if not x in range(max(lst)):
        return []

    # sort by rows starting with the row at index
    lst.sort()
    if not isinstance(x, int):
        print("Bad input: " + str(type(x)))
    elif type(x) is int and x < 0 or x > max(lst)+1: # no duplicates and all integers
        return []
    
    # we don't have to sort by columns, since they will be sorted
    # when the rows are sorted
    
    lst.sort()
    if type(x) is int and (x < 0 or x > max(lst)+1):
        return []
    else:
        return [(i,j) for j in range(max(lst)) for i in range(max(lst)-1)]
    
def sum_all_rows(lst, n):
    """
    Similar to get_row, you are