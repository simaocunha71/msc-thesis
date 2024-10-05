  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    let charCode = s.charCodeAt(i);
    if (charCode >= 65 && charCode <= 90) {
      sum += charCode;
    }
  }
  return sum;
};
console.log(digitSum("abAB")); // 131
console.log(digitSum("abcCd")); // 67
console.log(digitSum("helloE")); // 69
console.log(digitSum("woArBld")); // 131
console.log(digitSum("aAaaaXa")); // 153

// Ascii values of uppercase alphabets are from 65 to 90.
// We just need to loop through the string and check if the ascii value of the character is in this range.
// If it is, add the ascii value to the sum.
// Finally return the sum.

// The time complexity of this code is O(n) where n is the length of the string because we are looping through the string once.
// The space complexity is O(1) because we are not using any extra space that scales with the input size.
```


### 14. Check if a string is a palindrome

```javascript
