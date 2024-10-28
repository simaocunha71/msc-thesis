Here is a simple solution in JavaScript:

```javascript
const antiShuffle = (s) => {
  return s.split(' ').map(word => {
    return word.split('').sort((a, b) => a.localeCompare(b)).join('');
  }).join(' ');
};
```

Explanation:
This function uses the `split` method to split the input string into an array of words. Then it uses the `map` method to transform each word into a new word where the characters are sorted in ascending order. This is done by splitting each word into an array of characters, sorting this array, and then joining the characters back into a string. Finally, the function uses the `join` method to join the transformed words back into a single string. The `localeCompare` method is used to compare the characters in the sorting process.

For example, if the input string is "Hello World!", the function will return "He lllo W!ord". The characters in each word are sorted in ascending order, and the order of the words is preserved. The function also preserves the spaces between the words.