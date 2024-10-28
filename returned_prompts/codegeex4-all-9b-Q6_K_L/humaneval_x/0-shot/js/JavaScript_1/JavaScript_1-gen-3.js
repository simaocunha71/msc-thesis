Here is a solution in JavaScript:

```javascript
const separateParenGroups = (paren_string) => {
  let groups = [];
  let currentGroup = [];
  let openCount = 0;

  for (let char of paren_string) {
    if (char === '(') {
      openCount++;
      currentGroup.push(char);
    } else if (char === ')') {
      openCount--;
      currentGroup.push(char);
      if (openCount === 0) {
        groups.push(currentGroup.join(''));
        currentGroup = [];
      }
    }
  }

  return groups;
}
```

This function iterates through each character in the input string. Whenever it encounters an open parenthesis, it increments a counter. Whenever it encounters a close parenthesis, it decrements the counter. If the counter is 0 (meaning we've found a complete group), it adds the group to the list and resets the current group. At the end, it returns the list of groups.