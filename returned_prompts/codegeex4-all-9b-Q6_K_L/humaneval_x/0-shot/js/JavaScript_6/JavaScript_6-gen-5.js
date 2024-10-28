```js
  const groups = paren_string.split(' ');
  const results = [];
  for (let group of groups) {
    let maxDepth = 0;
    let currentDepth = 0;
    for (let char of group) {
      if (char === '(') {
        currentDepth += 1;
        if (currentDepth > maxDepth) {
          maxDepth = currentDepth;
        }
      } else if (char === ')') {
        currentDepth -= 1;
      }
    }
    results.push(maxDepth);
  }
  return results;
}
```