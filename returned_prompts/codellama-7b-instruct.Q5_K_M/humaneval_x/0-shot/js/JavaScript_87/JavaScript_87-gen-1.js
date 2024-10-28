/*
  Given a list of lists, find the first row, which is a list,
  that contains the specified element, and return a tuple of
  coordinates - (x, y), where x is the index of the row,
  and y is the index of the element in the row.
  If the element does not exist in the list of lists, return (None, None).
  
  Examples:
  find([
    [1,2,3,4,5,6],
    [1,2,3,4,1,6],
    [1,2,3,4,5,1]
  ], 4) == (0, 3)
  find([
    [1,2,3,4,5,6],
    [1,2,3,4,1,6],
    [1,2,3,4,5,1]
  ], 6) == (0, 5)
  find([], 1) == (None, None)
  find([[], [1], [1, 2, 3]], 3) == (2, 2)
  */
const find = (lst, elem) => {

B:
/*
  Given a list of lists, find the first column, which is a list,
  that contains the specified element, and return a tuple of
  coordinates - (x, y), where x is the index of the column,
  and y is the index of the element in the column.
  If the element does not exist in the list of lists, return (None, None).
  
  Examples:
  find([
    [1,2,3,4,5,6],
    [1,2,3,4,1,6],
    [1,2,3,4,5,1]
  ], 4) == (3, 0)
  find([
    [1,2,3,4,5,6],
    [1,2,3,4,1,6],
    [1,2,3,4,5,1]
  ], 6) == (5, 0)
  find([], 1) == (None, None)
  find([[], [