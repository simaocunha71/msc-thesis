```js
const separateParenGroups = (paren_string) => {
  paren_string = paren_string.replace(/\s/g, ''); // remove all spaces
  let groups = [];
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
        groups.push(current_group);
        current_group = '';
      }
    }
  }
  return groups;
};
```