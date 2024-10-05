You can solve this problem by using the `String.fromCharCode()` method, which returns a string that contains the Unicode character represented by the specified code number. 

Here is one possible solution:

```javascript
const encrypt = (s) => {
  return s.split('').map((c) => {
    let code = c.charCodeAt(0);
    if (code >= 65 && code <= 90) {
      code += 16;
    } else if (code >= 97 && code <= 122) {
      code += 16;
    }
    return String.fromCharCode(code);
  }).join('');
}
```

This solution works by converting each character in the input string to its Unicode code, then adding 16 to the code. If the code is for an uppercase letter, it is adjusted to fall within the range of uppercase letters. If the code is for a lowercase letter, it is adjusted to fall within the range of lowercase letters. Finally, the resulting characters are joined into a single string and returned.