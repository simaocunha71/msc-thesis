```javascript
const parseNestedParens = (paren_string) => {
  const groups = paren_string.split(' ');
  const results = [];
  for (const group of groups) {
    let deepestLevel = 0;
    let currentLevel = 0;
    for (const char of group) {
      if (char === '(') {
        currentLevel++;
        deepestLevel = Math.max(deepestLevel, currentLevel);
      } else if (char === ')') {
        currentLevel--;
      }
    }
    results.push(deepestLevel);
  }
  return results;
};
console.log(parseNestedParens('(()()) ((())) () ((())()())'));
// Output: [2, 3, 1, 3]
```
In this code, we first split the input string into groups by spaces. Then for each group, we initialize two variables: `deepestLevel` to keep track of the deepest level of nesting found so far, and `currentLevel` to keep track of the current level of nesting. We iterate over each character in the group, and for each `(`, we increment `currentLevel` and update `deepestLevel` if `currentLevel` is greater than `deepestLevel`. For each `)`, we decrement `currentLevel`. Finally, we add the `deepestLevel` for each group to the result array. The function returns the result array. The example output `[2, 3, 1, 3]` means the deepest level of nesting for the first group is 2, for the second group is 3, and so on.