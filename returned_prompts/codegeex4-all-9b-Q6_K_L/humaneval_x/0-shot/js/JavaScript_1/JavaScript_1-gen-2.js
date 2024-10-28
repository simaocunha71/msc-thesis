Here is a solution using JavaScript:

```javascript
const separateParenGroups = (paren_string) => {
  let result = [];
  let current_string = '';
  let open_braces = 0;

  for (let i = 0; i < paren_string.length; i++) {
    let char = paren_string[i];

    if (char === '(') {
      open_braces++;
    } else if (char === ')') {
      open_braces--;
    }

    if (open_braces === 0) {
      result.push(current_string);
      current_string = '';
    } else {
      current_string += char;
    }
  }

  return result;
}
```

In this solution, we iterate over each character in the input string. If the character is an open brace, we increment the `open_braces` counter. If the character is a closed brace, we decrement the `open_braces` counter. If the `open_braces` counter reaches 0, we have completed a separate group of parentheses, so we add it to the result array and reset the `current_string` and `open_braces` variables. Otherwise, we add the character to the `current_string`.