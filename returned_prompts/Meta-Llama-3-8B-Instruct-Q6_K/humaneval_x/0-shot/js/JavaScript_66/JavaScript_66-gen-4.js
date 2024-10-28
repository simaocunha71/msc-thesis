Here is the JavaScript solution for the problem:

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
The function `digitSum` takes a string `s` as input and initializes a variable `sum` to 0. It then iterates over each character `char` in the string using a for...of loop.

 Inside the loop, it checks if the character is uppercase by comparing it to its uppercase version using the `toUpperCase` method. If the character is uppercase, it adds its ASCII code (obtained using the `charCodeAt` method) to the `sum`.

 Finally, the function returns the `sum` which is the sum of the upper characters only' ASCII codes.

Note: The `charCodeAt` method returns the Unicode code point of the character at the specified index. In this case, we pass 0 as the index because we want the code point of the character itself, not a character at a specific position in the string.