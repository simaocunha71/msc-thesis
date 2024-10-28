```js
  const parenGroups = paren_string.split(' ');
  const nestedLevels = parenGroups.map(group => {
    let level = 0;
    let maxLevel = 0;
    for (let i = 0; i < group.length; i++) {
      if (group[i] === '(') {
        level++;
        maxLevel = Math.max(maxLevel, level);
      } else if (group[i] === ')') {
        level--;
      }
    }
    return maxLevel;
  });
  return nestedLevels;
}
```