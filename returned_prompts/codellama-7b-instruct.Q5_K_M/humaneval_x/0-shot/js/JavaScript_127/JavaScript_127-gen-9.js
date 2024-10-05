/*
  Given two sorted arrays of integers, find the smallest index in the first array
  where the value should be inserted to maintain the order of the second array.

  [input/output] samples:
  findSmallestIndex([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]) ==> 0
  findSmallestIndex([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]) ==> 6
  findSmallestIndex([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7]) ==> 6
  findSmallestIndex([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5]) ==> 5
  findSmallestIndex([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]) ==> 5
  findSmallestIndex([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]) ==> 5
  findSmallestIndex([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]) ==> 5
  findSmallestIndex([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]) ==> 5
  findSmallestIndex([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]) ==> 5
  findSmallestIndex([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]) ==> 5
  findSmallestIndex([1, 2, 3,