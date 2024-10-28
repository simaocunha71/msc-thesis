Here is a possible implementation of the `separateParenGroups` function in JavaScript:
```
const separateParenGroups = (paren_string) => {
  const groups = [];
  let currentGroup = '';
  let depth = 0;

  for (let i = 0; i < paren_string.length; i++) {
    const char = paren_string[i];
    if (char === '(') {
      depth++;
      currentGroup += char;
    } else if (char === ')') {
      depth--;
      currentGroup += char;
      if (depth === 0) {
        groups.push(currentGroup);
        currentGroup = '';
      }
    }
  }

  return groups;
};
```
Here's an explanation of how the function works:

1. We initialize an empty array `groups` to store the separated groups of parentheses.
2. We initialize a variable `currentGroup` to store the current group of parentheses being built.
3. We initialize a variable `depth` to keep track of the nesting level of the parentheses.
4. We iterate through the input string character by character.
5. If we encounter an opening parenthesis `(`, we increment the `depth` variable and add the parenthesis to the `currentGroup`.
6. If we encounter a closing parenthesis `)`, we decrement the `depth` variable and add the parenthesis to the `currentGroup`. If the `depth` variable becomes 0, it means we have finished building a group of parentheses, so we add the `currentGroup` to the `groups` array and reset `currentGroup` to an empty string.
7. Finally, we return the `groups` array.

You can test this function with the example input you provided:
```
console.log(separateParenGroups('( ) (( )) (( )( ))'));
// Output: ["()", "(())", "(()())"]
```
I hope this helps! Let me know if you have any questions.