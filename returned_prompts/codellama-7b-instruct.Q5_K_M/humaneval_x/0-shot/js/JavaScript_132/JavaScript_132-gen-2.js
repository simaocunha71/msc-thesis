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
  let arr = string.split('');
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === '[') {
      count++;
    }
    if (arr[i] === ']') {
      count--;
    }
    if (count < 0) return false;
  }
  return count === 0 ? true : false;
}
