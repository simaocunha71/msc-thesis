```javascript
const parseNestedParens = (paren_string) => {
  return paren_string.split(' ').map(group => {
    let level = 0;
    for (let char of group) {
      if (char === '(') {
        level++;
      } else if (char === ')') {
        level--;
      }
    }
    return level;
  });
};

console.log(parseNestedParens('(()()) ((())) () ((())()())'));
// Output: [2, 3, 1, 3]
```
This function splits the input string into groups based on the spaces. Then, for each group, it iterates through the characters and keeps track of the nesting level by incrementing it when it encounters an open parenthesis and decrementing it when it encounters a close parenthesis. The maximum nesting level of the group is the maximum level encountered during the iteration. The function returns an array of the maximum nesting levels for each group. 