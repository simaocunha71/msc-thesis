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
Explanation:
The task is to create a function that takes a string as input and returns the sum of the ASCII codes of the upper case characters only.

The function `digitSum` iterates over each character in the input string `s`. For each character, it checks if the character is equal to its upper case version using the `toUpperCase` method. If the character is upper case, it adds the ASCII code of the character to the `sum` variable using the `charCodeAt` method.

Finally, the function returns the `sum` variable, which holds the sum of the ASCII codes of the upper case characters in the input string.

Note that the `charCodeAt` method returns the ASCII code of the character at the specified index, which in this case is always 0 since we're not iterating over a specific index. The `toUpperCase` method is used to check if the character is upper case, and if it is, we add its ASCII code to the sum. If the character is not upper case, we skip it and move on to the next character.