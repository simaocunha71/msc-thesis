The `parseNestedParens` function can be implemented in JavaScript as follows:

```javascript
const parseNestedParens = (paren_string) => {
  const groups = paren_string.split(' ');
  const maxLevels = [];

  for (let group of groups) {
    let level = 0;
    let maxLevel = 0;
    for (let char of group) {
      if (char === '(') {
        level += 1;
        maxLevel = Math.max(level, maxLevel);
      } else if (char === ')') {
        level -= 1;
      }
    }
    maxLevels.push(maxLevel);
  }

  return maxLevels;
};
```

This function first splits the input string into groups of parentheses. Then, for each group, it iterates through the characters and maintains the current level of nesting of parentheses. It keeps track of the maximum level of nesting encountered for each group. Finally, it returns an array of maximum levels for each group.