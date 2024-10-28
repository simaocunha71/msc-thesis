The solution is to traverse the string and replace spaces accordingly. Here is the step-by-step approach:

1. Create an empty string `result` to store the final string.
2. Create a counter `spaceCount` to count consecutive spaces.
3. Traverse the string `text`:
   - If the current character is a space, increment `spaceCount` by 1 and continue to the next character.
   - If the current character is not a space and `spaceCount` is less than 2, add all spaces to `result` and reset `spaceCount` to 0.
   - If the current character is not a space and `spaceCount` is greater than or equal to 2, add `-` to `result` and reset `spaceCount` to 0.
   - Add the current character to `result`.
4. If `spaceCount` is greater than 0 after traversing the string, add `-` to `result`.
5. Return `result`.

Here is the implementation of the `fixSpaces` function:

```javascript
const fixSpaces = (text) => {
  let result = '';
  let spaceCount = 0;

  for (let i = 0; i < text.length; i++) {
    if (text[i] === ' ') {
      spaceCount++;
      continue;
    }

    if (spaceCount < 2) {
      for (let j = 0; j < spaceCount; j++) {
        result += ' ';
      }
    } else {
      result += '-';
    }

    spaceCount = 0;
    result += text[i];
  }

  if (spaceCount > 0) {
    result += '-';
  }

  return result;
};
```