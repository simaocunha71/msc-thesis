```javascript
const flipCase = (string) => {
  let newString = '';
  for (let i = 0; i < string.length; i++) {
    if (string[i] === string[i].toLowerCase()) {
      newString += string[i].toUpperCase();
    } else {
      newString += string[i].toLowerCase();
    }
  }
  return newString;
};
```
