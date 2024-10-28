```
function solve(s) {
  let result = '';
  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (char.match(/[a-zA-Z]/)) {
      result += char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase();
    } else {
      result += char;
    }
  }
  return result.split('').reverse().join('');
}
```


This solution iterates over the input string and checks if each character is a letter using a regular expression. If it is, it reverses its case using the `toUpperCase()` and `toLowerCase()` methods. If the character is not a letter, it leaves it as it is. Finally, it reverses the resulting string using the `split()`, `reverse()`, and `join()` methods. The `split('')` method splits the string into an array of individual characters, the `reverse()` method reverses the array, and the `join('')` method joins the array back into a string. The resulting string is then returned as the solution.