Here is the JavaScript code to solve the problem:

```javascript
const parseNestedParens = (paren_string) => {
  let paren_groups = paren_string.split(" ");
  let max_levels = [];

  for (let i = 0; i < paren_groups.length; i++) {
    let level = 0;
    let max_level = 0;
    for (let j = 0; j < paren_groups[i].length; j++) {
      if (paren_groups[i][j] === "(") {
        level++;
        max_level = Math.max(level, max_level);
      } else if (paren_groups[i][j] === ")") {
        level--;
      }
    }
    max_levels.push(max_level);
  }

  return max_levels;
};
```

In this code, we first split the input string into an array of parentheses groups. Then we iterate over each group and count the number of open parentheses. If the current character is an open parenthesis, we increment the level and update the maximum level if necessary. If the current character is a close parenthesis, we decrement the level. At the end of each group, we push the maximum level to the `max_levels` array. Finally, we return the `max_levels` array.