
/*
  Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

  For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

  Follow-up: what if you can't use division?

  O(n) time and O(n) space
  */
  const getProducts = (nums) => {
    const products = [];
    for (let i = 0; i < nums.length; i++) {
      products[i] = 1;
      for (let j = 0; j < nums.length; j++) {
        if (j !== i) {
          products[i] *= nums[j];
        }
      }
    }
    return products;
  };

B:

/*
  You are given a string of round, curly, and square open and closing brackets.
  Return whether the order of these brackets is valid.

  We consider two types of brackets:

  -  "(": round brackets
  -  "{": curly brackets
  -  "[": square brackets
  When a bracket is open, it means that we have not yet closed it.

  For example, in the string "([)]", we have not yet closed the opening "(", so it is still open.
  The string "[(])" is also invalid, since we have opened and not closed the opening "(", so it is still open.
  However, the string "[()]" is valid, since we have opened and closed all of our brackets.

  Another example, the string "([{}])" is valid, since all of our brackets are matched with the correct one.

  Note that only the three types of brackets mentioned above are used in this problem.
  The input string will only contain the three types of brackets.
  */

  const isValid = (s) => {
