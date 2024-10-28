  let s = lst.join('');
  let stack = [];

  for (let i = 0; i < s.length; i++) {
    if (s[i] === '(') {
      stack.push(s[i]);
    } else {
      if (!stack.length) {
        return 'No';
      }
      stack.pop();
    }
  }

  return stack.length ? 'No' : 'Yes';
}

console.log(matchParens(['()(', ')'])) // 'Yes'
console.log(matchParens([')', ')'])) // 'No'
```

This solution works by iterating over the string and pushing any '(' characters to a stack. If it encounters a ')' character, it checks if the stack is empty. If the stack is empty, it means there is no matching '(', and it returns 'No'. If the stack is not empty, it pops the top element from the stack. After iterating over all the characters in the string, it checks if there are any remaining elements in the stack. If there are, it means there are unmatched '(', and it returns 'No'. Otherwise, it means all parentheses are balanced, and it returns 'Yes'.

This solution has a time complexity of O(n), where n is the length of the string.

This solution has a space complexity of O(n), where n is the length of the string.
*/

// Do not edit this line;
module.exports = matchParens;



























































































































































