Here is the JavaScript code for the problem:

```javascript
const antiShuffle = (s) => {
  return s.split(' ').map(word => {
    return [...word].sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('');
  }).join(' ');
};
```

Explanation:
This function works by splitting the input string into an array of words using the `split` method. Then, for each word, it converts the word into an array of characters using the spread operator `...`, sorts the array of characters using the `sort` method, and then joins the sorted array back into a string using the `join` method. Finally, it joins the array of sorted words back into a string using the `join` method.

The `sort` method is used to sort the characters in the word based on their ASCII values. The `charCodeAt` method is used to get the ASCII value of a character.

The `map` method is used to apply this process to each word in the array of words. The `join` method is used to join the array of sorted words back into a string.

For example, if the input string is `'Hello World!!!'`, the function will return `'Hello !!!Wdlor'`. If the input string is `'hello'`, the function will return `'ehllo'`. If the input string is `'Hi'`, the function will return `'Hi'`.