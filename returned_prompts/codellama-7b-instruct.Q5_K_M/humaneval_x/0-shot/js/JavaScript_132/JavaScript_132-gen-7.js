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
  let count = 0;
  let isNested = false;
  for (let i = 0; i < string.length; i++) {
    if (string[i] === "[") {
      count++;
      isNested = true;
    }
    if (string[i] === "]") {
      count--;
      isNested = true;
    }
    if (count < 0) {
      return false;
    }
  }
  return count > 0;
}
