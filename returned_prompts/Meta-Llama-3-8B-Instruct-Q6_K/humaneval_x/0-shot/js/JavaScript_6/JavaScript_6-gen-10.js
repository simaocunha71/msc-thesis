Here is the solution to the problem:
```
const parseNestedParens = (paren_string) => {
  const groups = paren_string.split(' ');
  const results = [];

  for (const group of groups) {
    let nestingLevel = 0;
    let maxNestingLevel = 0;

    for (const char of group) {
      if (char === '(') {
        nestingLevel++;
      } else if (char === ')') {
        nestingLevel--;
      }
      maxNestingLevel = Math.max(maxNestingLevel, nestingLevel);
    }

    results.push(maxNestingLevel);
  }

  return results;
};
```
Explanation:
The function `parseNestedParens` takes a string of parentheses groups as input and returns an array of the maximum nesting levels for each group.

Here's how it works:

1. First, we split the input string into individual groups using the `split` method with a space character as the separator.
2. We initialize an empty array `results` to store the maximum nesting levels for each group.
3. We iterate over each group using a `for` loop.
4. For each group, we initialize two variables: `nestingLevel` to keep track of the current nesting level, and `maxNestingLevel` to keep track of the maximum nesting level seen so far.
5. We iterate over each character in the group using another `for` loop.
6. For each character, we check if it's an opening parenthesis (`(`). If it is, we increment `nestingLevel`. If it's a closing parenthesis (`)`), we decrement `nestingLevel`.
7. We update `maxNestingLevel` to be the maximum of its current value and `nestingLevel`.
8. Finally, we push the maximum nesting level for the current group onto the `results` array.
9. We return the `results` array.

For example, if the input string is `'(()()) ((())) () ((())()())'`, the function will return the array `[2, 3, 1, 3]`, indicating that the deepest level of nesting for each group is 2, 3, 1, and 3, respectively.