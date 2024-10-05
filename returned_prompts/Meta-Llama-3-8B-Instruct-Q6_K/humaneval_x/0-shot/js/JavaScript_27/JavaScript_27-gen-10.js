```javascript
const flipCase = (string) => {
  return string.replace(/([a-z])/gi, match => match.toUpperCase())
             .replace(/([A-Z])/gi, match => match.toLowerCase());
};
```
Explanation:
We use the `replace()` method with a regular expression to achieve this. The regular expression `/([a-z])/gi` matches any lowercase letter (`[a-z]`) in the string, and the `gi` flag makes it case-insensitive. The callback function `match => match.toUpperCase()` converts each matched lowercase letter to uppercase.

Similarly, `/([A-Z])/gi` matches any uppercase letter, and `match => match.toLowerCase()` converts each matched uppercase letter to lowercase.

The `replace()` method is called twice, first for lowercase letters and then for uppercase letters, to achieve the desired output. The resulting string is then returned.