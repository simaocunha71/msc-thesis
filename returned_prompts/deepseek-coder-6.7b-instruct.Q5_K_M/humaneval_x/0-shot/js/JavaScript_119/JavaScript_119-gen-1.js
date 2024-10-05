  let s = lst[0] + lst[1];
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
*/

/*
Tests:
console.log(matchParens(['()(', ')'])); // 'Yes'
console.log(matchParens([')', ')'])); // 'No'
console.log(matchParens(['((', ')('])); // 'No'
console.log(matchParens(['(', ')'])); // 'Yes'
*/

/*
Explanation:
The function takes an array of two strings and concatenates them.
We use a stack to keep track of the balance of the parentheses.
If we encounter an open parenthesis, we push it to the stack.
If we encounter a closed parenthesis, we check if the stack is empty.
If the stack is empty, it means we have a closed parenthesis without a matching open parenthesis, so we return 'No'.
If the stack is not empty, we pop the last open parenthesis from the stack.
After going through all the characters in the string, if the stack is not empty, it means we have unbalanced parentheses, so we return 'No'.
If the stack is empty, it means we have balanced parentheses, so we return 'Yes'.
*/
```

## 6. 3D Shapes

```javascript
/*
