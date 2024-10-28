```
const decodeCyclic = (s) => {
  let result = '';
  for (let i = 0; i < s.length; i += 3) {
    if (i + 3 <= s.length) {
      result += s.slice(i, i + 3)[2] + s.slice(i, i + 3)[0] + s.slice(i, i + 3)[1];
    } else {
      result += s.slice(i);
    }
  }
  return result;
}
```


Here is the explanation:

1. The encodeCyclic function takes a string as input and returns a new encoded string. It works by grouping the characters in groups of three and then rearranging each group so that the last character becomes the first character, and the other two characters remain in their original order. If the string length is not a multiple of three, the remaining characters are appended to the end of the encoded string.

2. The decodeCyclic function takes an encoded string as input and returns the original decoded string. It works by iterating over the characters in the encoded string in groups of three. If a group has only two characters, it is appended to the decoded string as is. If a group has three characters, it is rearranged so that the first character becomes the last character, and the other two characters remain in their original order. If the encoded string has fewer than three characters left, they are appended to the decoded string as is.

Here is the code for the decodeCyclic function:

```javascript
const decodeCyclic = (s) => {
  let result = '';
  for (let i = 0; i < s.length; i += 3) {
    if (i + 3 <= s.length) {
      result += s.slice(i, i + 3)[2] + s.slice(i, i + 3)[0] + s.slice(i, i + 3)[1];
    } else {
      result += s.slice(i);
    }
  }
  return result;
}
```

This function uses the slice method to extract groups of three characters from the encoded string. If a group has three characters, it is rearranged using the syntax `s.slice(i, i + 3)[2] + s.slice(i, i + 3)[0] + s.slice(i, i + 3)[1]`. If a group has only two characters, it is appended to the decoded string as is. Finally, the decoded