```js
const parseNestedParens = (paren_string) => {
  const groups = paren_string.split(' ');
  return groups.map(group => {
    let level = 0;
    let maxLevel = 0;
    for (let i = 0; i < group.length; i++) {
      if (group[i] === '(') {
        level++;
        if (level > maxLevel) {
          maxLevel = level;
        }
      } else if (group[i] === ')') {
        level--;
      }
    }
    return maxLevel;
  });
}
```
