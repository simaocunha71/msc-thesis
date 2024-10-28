Here's one way you could write the removeVowels function:

```javascript
const removeVowels = (text) => {
  return text.replace(/[aeiou]/gi, '');
};
```

This function uses the `replace` method to replace all instances of vowels (both lower and upper case) in the input text with an empty string. The `/[aeiou]/gi` part is a regular expression that matches all vowel characters.

The `g` flag makes the `replace` method replace all occurrences of the vowels, not just the first one. The `i` flag makes the `replace` method case-insensitive, so it will remove both lowercase and uppercase vowels.

You can test this function with the provided test cases in the REPL:

```javascript
console.log(removeVowels(''));           // ''
console.log(removeVowels("abcdef\nghijklm")); // 'bcdf\nghjklm'
console.log(removeVowels('abcdef'));    // 'bcdf'
console.log(removeVowels('aaaaa'));     // ''
console.log(removeVowels('aaBAA'));     // 'B'
console.log(removeVowels('zbcd'));      // 'zbcd'
```

And you can experiment with other test cases as well.

This solution should be efficient and work well for most cases. However, keep in mind that regular expressions can be a bit slow for very large input strings. If you're dealing with very large strings and performance is a concern, you might want to consider alternative approaches, such as using a `for` loop to manually iterate through each character in the string.

Lastly, it's worth noting that this solution only removes vowels and does not handle other special characters or whitespace. If you need to remove other types of characters, you can modify the regular expression accordingly. For example, to remove all non-alphanumeric characters (including spaces), you could use `/[^a-zA-Z0-9]/g` as the replacement pattern in the `replace` method.

Overall, the provided solution should meet the requirements of the original question