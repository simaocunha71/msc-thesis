```javascript
const flipCase = (string) => {
  return string.replace(/([a-z])/g, match => match.toUpperCase())
               .replace(/([A-Z])/g, match => match.toLowerCase());
};
```

Explanation:
The `replace()` function is used to replace specific characters in the string. The regular expression `/([a-z])/g` matches any lowercase letter (captured in a group), and the `match => match.toUpperCase()` function is called for each match, which converts the lowercase letter to uppercase.

Similarly, the regular expression `/([A-Z])/g` matches any uppercase letter (captured in a group), and the `match => match.toLowerCase()` function is called for each match, which converts the uppercase letter to lowercase.

The two `replace()` calls are chained together to process the entire string. The result is a new string with all lowercase letters converted to uppercase and all uppercase letters converted to lowercase.