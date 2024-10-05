/*
  Given a number of rows and columns, return a list of lists,
  where each inner list contains number of rows elements.
  The outer list contains rows lists.
  If number of rows or columns is less than 1, return empty list.
  If number of rows or columns is invalid (less than 1)
  or greater than 1000, return list with single element - string.
  
  Examples:
  makeGrid(2, 2) == [[1, 2], [3, 4]]
  makeGrid(3, 2) == [[1, 2], [3, 4], [5, 6]]
  makeGrid(2, 3) == [[1, 2, 3], [4, 5, 6]]
  makeGrid(1, 1) == [[1]]
  makeGrid(0, 0) == []
  makeGrid(1, 0) == ['Matrix size out of range']
  makeGrid(1001, 1001) == ['Matrix size out of range']
  */
const makeGrid = (rows, cols) => {

