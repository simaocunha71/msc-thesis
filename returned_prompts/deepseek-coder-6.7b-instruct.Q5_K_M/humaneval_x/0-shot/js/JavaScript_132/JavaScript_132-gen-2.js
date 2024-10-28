  let stack = [];

  for (let i = 0; i < string.length; i++) {
    if (string[i] === '[') {
      stack.push(string[i]);
    } else {
      if (stack.length === 0) {
        return false;
      }
      stack.pop();
    }
  }

  return stack.length === 0 ? false : true;
}

console.log(isNested('[[]]')); // ➞ true
console.log(isNested('[]]]]]]][[[[[]')); // ➞ false
console.log(isNested('[][]')); // ➞ false
console.log(isNested('[]')); // ➞ false
console.log(isNested('[[][]]')); // ➞ true
console.log(isNested('[[]][[')); // ➞ true

This solution uses a stack data structure to keep track of the opening brackets. As we iterate through the string, if we find an opening bracket, we push it to the stack. If we find a closing bracket, we pop the last element from the stack. If at any point the stack is empty and we find a closing bracket, we return false. If the stack is not empty at the end of the iteration, we return false because there is an unpaired opening bracket. If the stack is empty at the end of the iteration, we return true.

The time complexity of this solution is O(n) as we iterate through the string once. The space complexity is also O(n) in the worst case scenario where all the brackets are opening brackets and we push them all to the stack.
*/

/*
  Create a function that takes a string as input which contains only square brackets.
  The function should return true if and only if there is a valid subsequence of brackets
  where at least one bracket in the subsequence is nested.
  isNested('[[]]') ➞ true
  isNested('[]]]]]]][[[[[]') ➞ false
  isNested('[][]') ➞ false
  isNested('[]') ➞