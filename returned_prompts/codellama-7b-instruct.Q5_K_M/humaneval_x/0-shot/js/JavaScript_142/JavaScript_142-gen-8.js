
/*
  The function should take in an array of integers. It should then iterate through each index of the array, squaring the value if the index is
  a multiple of 3 or cubing the value if the index is a multiple of 4. It should return the sum of the squared or cubed values.

  Pseudocode:
  let sum = 0;
  for each element in the array
    if the index is a multiple of 3
      square the value
    if the index is a multiple of 4
      cube the value
    add the squared or cubed value to the sum
  return the sum
*/

/*
  Test case 1:
  Input: lst = [1,2,3]
  Output: 6
  Expected: 1^2 + 8 + 27 = 36

  Test case 2:
  Input: lst = []
  Output: 0
  Expected: []

  Test case 3:
  Input: lst = [-1,-5,2,-1,-5]
  Output: -126
  Expected: -1^2 + (-5)^3 + 16 + (-1)^2 + (-5)^3 = -126
*/

};

// top vote solution
const sumSquares = (lst) => lst.map((v, i) => (i % 3 ? v : v ** 2) * (i % 4 ? v : v ** 3)).reduce((a, v) => a + v, 0);
