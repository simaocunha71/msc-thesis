```javascript
function solve(s) {
  let result = '';
  for (let i = 0; i < s.length; i++) {
    if (s[i].toLowerCase() >= 'a' && s[i].toLowerCase() <= 'z') {
      result += s[i].toUpperCase() === s[i] ? s[i].toLowerCase() : s[i].toUpperCase();
    } else {
      result += s[i];
    }
  }
  return result.split('').reverse().join('');
}
```


Explanation:
This function iterates over the input string `s`. For each character, it checks if it's a letter using the `toLowerCase` method. If it is a letter, it reverses its case using the `toUpperCase` method. If it's not a letter, it simply adds it to the result string. After processing all characters, it reverses the result string using the `split`, `reverse`, and `join` methods. The resulting string is then returned.