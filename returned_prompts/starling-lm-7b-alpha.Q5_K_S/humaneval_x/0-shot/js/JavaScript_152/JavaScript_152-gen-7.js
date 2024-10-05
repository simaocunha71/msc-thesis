  let result = [];

  for (let i = 0; i < game.length; i++) {
    result.push(Math.abs(game[i] - guess[i]));
  }

  return result;
};


//----------------------------------------------------------------------------------------------------------------------------------------------------------

/*
  Create a function that takes an array of numbers and an array of operations as parameters.
  The function should return the result of applying each operation to the number array.
  The operations can be "add", "subtract", "multiply" or "divide".
  For example, if the number array is [1, 2, 3, 4, 5] and the operations array is ["add", "+", 10],
  the function should return a new array [11, 12, 13, 14, 15].

  You can assume that the operations array is always valid (i.e. it always contains exactly three elements, and the third element is either a number or a string).
  Also, you can assume that the first element of the operations array is either "add", "subtract", "multiply" or "divide".
  The second element of the operations array is either "+" or "-" or "*" or "/".
  The third element of the array is a number.

  Here are some more examples to clarify:

  applyOps([1,2,3,4,5], ["add", "+", 10]) -> [11, 12, 13, 14, 15]
  applyOps([1,2,3,4,5], ["multiply", "*", 10]) -> [10, 20, 30, 40, 50]
  applyOps([1,2,3,4,5], ["divide", "/", 10]) -> [0.1, 0.2, 0.3, 0.4, 0.5]

  Note that in the third example, the result of the division is rounded to two decimal places.

  The function should return a new array. The original number array should not be modified.

*/

const applyOps = (nums,