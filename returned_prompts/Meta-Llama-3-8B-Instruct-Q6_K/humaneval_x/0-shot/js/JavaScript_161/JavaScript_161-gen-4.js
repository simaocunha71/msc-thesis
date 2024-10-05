```javascript
const result = [];

for (let i = 0; i < s.length; i++) {
  const char = s[i];
  if (char.match(/[a-zA-Z]/)) { // check if char is a letter
    result.push(char.toUpperCase()); // reverse case
  } else {
    result.push(char); // keep it as it is
  }
}

return result.join(''); // join the result array into a string
``` 