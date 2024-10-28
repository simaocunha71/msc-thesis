The problem asks to write a function that takes a string as input and returns the sum of the ASCII codes of the upper characters only.

Here is a JavaScript solution for the problem:

```javascript
const digitSum = (s) => {
  let sum = 0;
  for(let i = 0; i < s.length; i++) {
    if(s[i].toUpperCase() === s[i]) {
      sum += s[i].charCodeAt(0);
    }
  }
  return sum;
};
```

In this solution, we initialize a variable `sum` to 0. Then, we loop through each character in the string using a for loop. For each character, we check if it is an uppercase character using the `toUpperCase()` method and compare it with the original character using the `===` operator. If they are the same, it means the character is uppercase, and we add its ASCII code to the `sum` using the `charCodeAt(0)` method. Finally, we return the `sum`.

This solution works for all the examples provided in the problem statement. For example, `digitSum("abAB")` returns 131, `digitSum("abcCd")` returns 67, and so on. The function correctly sums up the ASCII codes of the uppercase characters only, ignoring the lowercase characters.