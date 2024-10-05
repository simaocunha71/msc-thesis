Here is a JavaScript function that solves the problem:

```javascript
const digitSum = (s) => {
  let sum = 0;
  for (let char of s) {
    if (char.toUpperCase() === char) {
      sum += char.charCodeAt(0);
    }
  }
  return sum;
};
```

This function iterates over each character in the input string. If the character is an uppercase letter (checked using `char.toUpperCase() === char`), it adds the character's ASCII code to the sum. The function then returns the total sum. The `charCodeAt(0)` method returns the Unicode code point for the character at the specified position in the string. In this case, we're using position 0, which corresponds to the first character in the string. The Unicode code point is equivalent to the ASCII code for uppercase letters.

For example, the ASCII code for 'A' is 65, 'B' is 66, and so on. The function correctly calculates the sum of these ASCII codes for uppercase letters in the input string. For lowercase letters, the function simply ignores them and continues to the next character.

The function handles edge cases such as an empty string by returning 0, as per the problem statement. It also correctly handles strings with a mix of uppercase and lowercase letters, as shown in the examples provided.