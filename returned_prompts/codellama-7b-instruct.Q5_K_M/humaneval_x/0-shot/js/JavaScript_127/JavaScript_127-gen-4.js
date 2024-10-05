/*You are given two non-empty arrays of integers,
  and an integer representing the number of operations.
  Your task is to sort the arrays and then perform
  the specified number of operations.
  Then, return an array of two integers representing
  the sum of the two sorted arrays.

  [input/output] samples:
  sortAndSum([1, 3, 5, 7], [2, 4, 6, 8], 2)
  ==> [7, 9, 11, 13]

  sortAndSum([1, 3, 5, 7], [2, 4, 6, 8], 1)
  ==> [5, 9, 13, 17]

  sortAndSum([1, 3, 5, 7], [2, 4, 6, 8], 0)
  ==> [1, 3, 5, 7, 2, 4, 6, 8]
  */
const sortAndSum = (arr1, arr2, numOps) => {

