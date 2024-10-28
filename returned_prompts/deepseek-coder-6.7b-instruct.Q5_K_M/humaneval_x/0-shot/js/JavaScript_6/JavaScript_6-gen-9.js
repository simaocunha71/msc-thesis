  let groups = paren_string.split(' ');
  let max_nesting_levels = [];

P:
  for (let group of groups) {
    let count = 0;
    let max = 0;
    for (let char of group) {
      if (char === '(') {
        count += 1;
        if (count > max) {
          max = count;
        }
      } else if (char === ')') {
        count -= 1;
      }
    }
    max_nesting_levels.push(max);
  }

  return max_nesting_levels;
};

console.log(parseNestedParens('(()()) ((())) () ((())()())'));
```

#### B)

```javascript
