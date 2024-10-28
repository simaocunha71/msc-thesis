```javascript
const separateParenGroups = (paren_string) => {
  // remove spaces from the input string
  paren_string = paren_string.replace(/\s/g, '');

  let result = [];
  let current_group = '';
  let open_braces = 0;

  for (let i = 0; i < paren_string.length; i++) {
    if (paren_string[i] === '(') {
      open_braces++;
      current_group += paren_string[i];
    } else if (paren_string[i] === ')') {
      open_braces--;
      current_group += paren_string[i];
      if (open_braces === 0) {
        result.push(current_group);
        current_group = '';
      }
    }
  }

  return result;
};
```

This solution iterates through the input string and keeps track of the number of open braces. When the number of open braces reaches zero, it means that a balanced group of parentheses has been found, so it is added to the result array. The current group is then reset and the iteration continues until the end of the string.