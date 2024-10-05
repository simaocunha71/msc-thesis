Here is the solution using JavaScript:

```javascript
const encrypt = (s) => {
  let result = '';
  for(let i = 0; i < s.length; i++) {
    let charCode = s.charCodeAt(i);
    if(charCode >= 65 && charCode <= 90) {
      // uppercase letter
      result += String.fromCharCode((charCode + 2 * 2) % 26 + 65);
    } else if(charCode >= 97 && charCode <= 122) {
      // lowercase letter
      result += String.fromCharCode((charCode + 2 * 2) % 26 + 97);
    } else {
      result += s[i];
    }
  }
  return result;
};
```

In this function, we iterate over each character in the input string. If the character is an uppercase letter (65-90), we calculate the new character code by adding 2 * 2 to the original character code and taking the modulus of 26 to ensure we stay within the range of uppercase letters. We then convert this character code back to a character using `String.fromCharCode`. We do the same for lowercase letters (97-122). If the character is not a letter, we simply add it to the result as is. Finally, we return the encrypted string. 