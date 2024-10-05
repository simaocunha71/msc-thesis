```javascript
const splitWords = (txt) => {
  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    return txt.split(',');
  } else {
    let count = 0;
    for (let i = 0; i < txt.length; i++) {
      if (txt[i].toLowerCase() >= 'a' && txt[i].toLowerCase() <= 'z' && (txt[i].toLowerCase().charCodeAt(0) - 'a'.charCodeAt(0)) % 2 !== 0) {
        count++;
      }
    }
    return count;
  }
};
```


Test cases:
```javascript
console.log(splitWords("Hello world!")); // ["Hello", "world!"]
console.log(splitWords("Hello,world!")); // ["Hello", "world!"]
console.log(splitWords("abcdef")); // 3
```


Explanation:
The function `splitWords` takes a string `txt` as an argument. It first checks if the string contains a space using the `includes` method. If it does, it splits the string into an array of words using the `split` method with a space as the separator.

If the string does not contain a space, it checks if it contains a comma using the `includes` method. If it does, it splits the string into an array of words using the `split` method with a comma as the separator.

If the string does not contain a space or a comma, it counts the number of lower-case letters with odd order in the alphabet. It does this by iterating over each character in the string, checking if it is a lower-case letter using the `toLowerCase` method, and if it is, checking if its ASCII code minus the ASCII code of 'a' is odd using the `charCodeAt` method. If it is, it increments a counter. Finally, it returns the count.