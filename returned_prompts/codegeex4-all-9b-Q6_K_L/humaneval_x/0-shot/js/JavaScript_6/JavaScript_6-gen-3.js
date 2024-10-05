```js
const parseNestedParens = (paren_string) => {
  const groups = paren_string.split(' ');
  return groups.map(group => {
    let depth = 0;
    let maxDepth = 0;
    for (let i = 0; i < group.length; i++) {
      if (group[i] === '(') {
        depth++;
        maxDepth = Math.max(depth, maxDepth);
      } else if (group[i] === ')') {
        depth--;
      }
    }
    return maxDepth;
  });
}
```