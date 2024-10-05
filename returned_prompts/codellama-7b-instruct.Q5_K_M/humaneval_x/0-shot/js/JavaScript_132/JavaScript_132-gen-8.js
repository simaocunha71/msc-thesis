/*
  Create a function that takes a string as input which contains only square brackets.
  The function should return true if and only if there is a valid subsequence of brackets
  where at least one bracket in the subsequence is nested.
  isNested('[[]]') ➞ true
  isNested('[]]]]]]][[[[[]') ➞ false
  isNested('[][]') ➞ false
  isNested('[]') ➞ false
  isNested('[[][]]') ➞ true
  isNested('[[]][[') ➞ true
  */
const isNested = (string) => {
  let stack = [];
  for (let bracket of string) {
    if (bracket === '[') {
      stack.push(bracket);
    } else {
      if (!stack.length) {
        return false;
      }
      stack.pop();
    }
  }
  return stack.length > 0;
};