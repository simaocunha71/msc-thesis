Here is the solution to the problem. This solution checks if the two strings can be concatenated in a way that the resulting string is balanced.

```javascript
const matchParens = (lst) => {
  const str1 = lst[0];
  const str2 = lst[1];
  const str = str1 + str2;
  let open = 0;
  let close = 0;

  for (let i = 0; i < str.length; i++) {
    if (str[i] === '(') open++;
    if (str[i] === ')') close++;

    if (close > open) return 'No';
  }

  if (open !== close) return 'No';

  return 'Yes';
};
```

In this solution, we first concatenate the two input strings into a single string. Then, we iterate through the string and count the number of open and close parentheses. If the number of close parentheses ever exceeds the number of open parentheses, we immediately return 'No', because this means that the string is not balanced. After iterating through the entire string, we check if the number of open and close parentheses is equal. If they are not equal, we return 'No', because this means that the string is not balanced. Otherwise, we return 'Yes', because this means that the string is balanced.