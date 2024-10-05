Here is the JavaScript solution for the problem:

```javascript
const antiShuffle = (s) => {
  return s.split(' ').map(word => [...word].sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('')).join(' ');
}
```

Explanation:
The function `antiShuffle` takes a string `s` as input. It splits the string into words using the `split` method with a space character as the separator. Then, it maps each word to a new string where the characters are arranged in ascending order based on their ASCII values using the `sort` method. The `join` method is used to concatenate the characters back into a string. Finally, the `join` method is used again to concatenate the words back into a string with spaces in between. The resulting string is returned. 

For example, if the input is `'Hello World!!!'`, the function will return `'Hello !!!Wdlor'`. If the input is `'hello'`, the function will return `'ehllo'`. If the input is `'Hi'`, the function will return `'Hi'`. 

This function assumes that the input string only contains spaces as word separators and does not contain any punctuation marks. If the input string can contain punctuation marks, you may need to add additional code to handle them. 