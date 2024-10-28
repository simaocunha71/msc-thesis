  let count = 0;
  for (let i = 0; i < string.length; i++) {
    if (string[i] === '[') count++;
    else count--;
    if (count < 0) return false;
  }
  return count > 0;
}
console.log(isNested('[[]]')); // ➞ true
console.log(isNested('[]]]]]]][[[[[]')); // ➞ false
console.log(isNested('[][]')); // ➞ false
console.log(isNested('[]')); // ➞ false
console.log(isNested('[[][]]')); // ➞ true
console.log(isNested('[[]][[')); // ➞ true
```

Explanation:
The function `isNested` counts the number of open and closed brackets in the string. If at any point the count goes negative, that means there is a closing bracket without a corresponding opening bracket, so it immediately returns `false`. If the count is positive at the end, that means there is at least one pair of brackets that were nested, so it returns `true`. If the count is zero at the end, that means there were no brackets in the string, so it returns `false`.

The time complexity of this function is O(n), where n is the length of the string, because it goes through the string once. The space complexity is O(1), because it only uses a single integer variable to keep track of the count of brackets.

This solution assumes that the input string is well-formed, i.e., it only contains square brackets and no other characters. If the input string can contain other characters, the function would need to be modified accordingly.
 */

// Do not edit below this line
module.exports = isNested;
