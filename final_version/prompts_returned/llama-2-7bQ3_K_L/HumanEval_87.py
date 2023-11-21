
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
    
    lst = list(lst)
    for i in range(len(list)):
        if len(lst[i]) != i:
            return [] # empty return means no coordinate in this row
        
    result = [(0, 0)]
    sorted_indices = list(range(1, i + 1)) # sorted indices of each row
    
    for index in sorted_indices[::-1]: # sort each rows by columns
        if len(lst[index]) == (index + 1):
            result.append((index, lst[index][len(lst[index]) - 1]))
    
    return result

def main():
    """
    Main function for the problem.
    """
    # Test case
    print("Test case: (26, 43)")
    lst = [[1, 2, 0], [5, 9, 1]]
    
    result = get_row(lst, 26)
   