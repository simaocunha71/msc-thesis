```javascript
const result = [];
for (let i = 0; i < s.length; i++) {
  if (s[i].match(/[a-zA-Z]/)) {
    result.push(s[i].toUpperCase() === s[i] ? s[i].toLowerCase() : s[i].toUpperCase());
  } else {
    result.push(s[i]);
  }
}
return result.join('');
```
Explanation:

The function `solve` takes a string `s` as input and returns the modified string. It iterates through each character in the string using a for loop. For each character, it checks if it's a letter using the `match` method with a regular expression. If it's a letter, it checks if it's in uppercase by comparing it to its uppercase version. If it's in uppercase, it converts it to lowercase and vice versa. If the character is not a letter, it simply adds it to the result array as it is. Finally, it joins the result array into a string and returns it.