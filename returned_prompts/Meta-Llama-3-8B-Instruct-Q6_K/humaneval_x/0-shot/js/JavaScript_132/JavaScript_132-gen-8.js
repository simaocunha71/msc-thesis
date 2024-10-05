Here is a possible solution:
```
const isNested = (string) => {
  let nestingLevel = 0;
  for (let char of string) {
    if (char === '[') {
      nestingLevel++;
    } else if (char === ']') {
      if (nestingLevel === 0) return false; // mismatched closing bracket
      nestingLevel--;
    }
  }
  return nestingLevel > 0; // at least one nested bracket
};
```
Here's an explanation of the solution:

1. We keep track of the current nesting level using the `nestingLevel` variable. It's initialized to 0.
2. We iterate through each character in the input string using a `for...of` loop.
3. If we encounter an opening bracket `['`, we increment the `nestingLevel`.
4. If we encounter a closing bracket `]`, we decrement the `nestingLevel`. If the `nestingLevel` becomes 0, it means we've found a mismatched closing bracket, so we return `false`.
5. After iterating through the entire string, we check if the `nestingLevel` is greater than 0. If it is, it means we've found at least one nested bracket, so we return `true`. Otherwise, we return `false`.

This solution has a time complexity of O(n), where n is the length of the input string, because we iterate through the string once. The space complexity is O(1), because we only use a constant amount of space to store the `nestingLevel` variable.