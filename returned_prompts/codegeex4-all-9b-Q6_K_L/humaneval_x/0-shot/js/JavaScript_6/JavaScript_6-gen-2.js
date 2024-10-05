```js
const parseNestedParens = (paren_string) => {
  return paren_string.split(' ').map(s => {
    let level = 0, max_level = 0;
    for (let c of s) {
      if (c === '(') {
        level += 1;
        max_level = Math.max(level, max_level);
      } else if (c === ')') {
        level -= 1;
      }
    }
    return max_level;
  });
}
```