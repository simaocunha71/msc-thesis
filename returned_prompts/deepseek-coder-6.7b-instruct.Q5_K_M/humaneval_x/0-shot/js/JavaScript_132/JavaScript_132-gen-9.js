  let stack = [];
  let foundNested = false;

  for (let i = 0; i < string.length; i++) {
    if (string[i] === "[") {
      stack.push(string[i]);
    } else {
      if (stack.length === 0) {
        return false;
      }
      let top = stack.pop();
      if (top !== "[") {
        return false;
      }
      foundNested = true;
    }
  }

  return foundNested && stack.length === 0;
}

console.log(isNested('[[]]')); // ➞ true
console.log(isNested('[]]]]]]][[[[[]')); // ➞ false
console.log(isNested('[][]')); // ➞ false
console.log(isNested('[]')); // ➞ false
console.log(isNested('[[][]]')); // ➞ true
console.log(isNested('[[]][[')); // ➞ true

```

This JavaScript solution works by traversing the input string from left to right, and using a stack to keep track of the bracket types we've seen so far.

If we encounter an opening bracket "[", we push it onto the stack.

If we encounter a closing bracket "]", we check if the stack is empty. If it is, that means there's no matching opening bracket for this closing bracket, so we return false.

Otherwise, we pop the last bracket from the stack, and if it's not an opening bracket "[", that means there's no matching opening bracket for this closing bracket, so we return false.

Finally, if we've made it through the entire string without returning false, that means we've found at least one pair of nested brackets, so we return true.

Remember that the stack should be empty at the end of the string to return true, as every opening bracket should have a corresponding closing bracket.

This solution has a time complexity of O(n) where n is the length of the string, and a space complexity of O(n) due to the use