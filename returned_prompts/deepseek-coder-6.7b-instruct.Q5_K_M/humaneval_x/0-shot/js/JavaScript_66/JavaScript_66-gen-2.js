  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    let charCode = s.charCodeAt(i);
    if (charCode >= 65 && charCode <= 90) {
      sum += charCode;
    }
  }
  return sum;
}

console.log(digitSum("abAB")); // 131
console.log(digitSum("abcCd")); // 67
console.log(digitSum("helloE")); // 69
console.log(digitSum("woArBld")); // 131
console.log(digitSum("aAaaaXa")); // 153

/*
  Explanation:
  This function works by iterating through each character in the input string and checking if the ASCII value of the character falls within the range for uppercase letters (65-90). If it does, the ASCII value is added to the sum. The sum is then returned.
*/
```

### Solution

```javascript
function digitSum(s) {
  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    let charCode = s.charCodeAt(i);
    if (charCode >= 65 && charCode <= 90) {
      sum += charCode;
    }
  }
  return sum;
}

console.log(digitSum("abAB")); // 131
console.log(digitSum("abcCd")); // 67
console.log(digitSum("helloE")); // 69
console.log(digitSum("woArBld")); // 131
console.log(digitSum("aAaaaXa")); // 153
```

In this solution, we define a function `digitSum()` that accepts a string `s`. We initialize a variable `sum` to 0, which will hold the total sum of the ASCII values of the uppercase characters in the string.

We then loop over each character in the string. For each character, we get its ASCII value using the `charCodeAt()`