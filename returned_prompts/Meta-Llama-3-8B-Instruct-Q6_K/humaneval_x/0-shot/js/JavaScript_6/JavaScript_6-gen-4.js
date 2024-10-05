Here is a simple and efficient solution using a stack to keep track of the nesting level. This function iterates over the input string, pushing each opening parenthesis onto the stack and popping it off when it encounters a closing parenthesis. The maximum stack size at any point during the iteration represents the deepest level of nesting for that group.

```javascript
const parseNestedParens = (paren_string) => {
  const paren_groups = paren_string.split(' ');
  return paren_groups.map(group => {
    let max_nesting = 0;
    let current_nesting = 0;
    for (let char of group) {
      if (char === '(') {
        current_nesting++;
      } else if (char === ')') {
        current_nesting--;
      }
      max_nesting = Math.max(max_nesting, current_nesting);
    }
    return max_nesting;
  });
};

console.log(parseNestedParens('(()()) ((())) () ((())()())'));
// Output: [2, 3, 1, 3]
```

This function splits the input string into groups separated by spaces, then maps over these groups to calculate the maximum nesting level for each group. The maximum nesting level is updated in each iteration of the loop, and the final result is an array of the maximum nesting levels for each group. The output for the example input is `[2, 3, 1, 3]`, which represents the deepest level of nesting for each group.