```js
const parseNestedParens = (paren_string) => {
  const paren_groups = paren_string.split(' ');
  const max_levels = [];
  for (let group of paren_groups) {
    let level = 0;
    let max_level = 0;
    for (let char of group) {
      if (char === '(') {
        level += 1;
        max_level = Math.max(level, max_level);
      } else if (char === ')') {
        level -= 1;
      }
    }
    max_levels.push(max_level);
  }
  return max_levels;
}
```