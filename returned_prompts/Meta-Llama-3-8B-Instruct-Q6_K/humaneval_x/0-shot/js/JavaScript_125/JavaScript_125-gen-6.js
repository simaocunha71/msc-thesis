Here is the solution for the problem:

```javascript
const splitWords = (txt) => {
  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    return txt.split(',');
  } else {
    let count = 0;
    for (let i = 0; i < txt.length; i++) {
      if (txt[i].toLowerCase() >= 'a' && txt[i].toLowerCase() <= 'z' && (txt[i].toLowerCase().charCodeAt(0) - 97) % 2 !== 0) {
        count++;
      }
    }
    return count;
  }
};
```
This function first checks if the input string contains a space. If it does, it splits the string into an array of words using the `split` method. If it does not, it checks if the string contains a comma. If it does, it splits the string into an array of words using the `split` method with a comma as the separator. If the string does not contain a space or a comma, it iterates over the characters in the string and counts the number of lowercase letters that have an odd index in the alphabet. The function returns this count.