Here is a JavaScript function that removes all vowels from a given string:

```javascript
function removeVowels(text) {
  const vowels = ["a", "e", "i", "o", "u"];
  return text.replace(/[aeiou]/gi, '');
}
```

The `replace` method is used with a regular expression that matches all vowels (both lowercase and uppercase), and the replacement string is an empty string, effectively removing the vowels.

Here are some test cases to verify the function works as expected:

```javascript
console.log(removeVowels(''));                      // ''
console.log(removeVowels("abcdef\nghijklm"));        // 'bcdf\nghjklm'
console.log(removeVowels('abcdef'));                // 'bcdf'
console.log(removeVowels('aaaaa'));                  // ''
console.log(removeVowels('aaBAA'));                  // 'B'
console.log(removeVowels('zbcd'));                   // 'zbcd'
```

The function correctly removes all vowels from the input string, regardless of their position or case.

Note: The `replace` method uses a regular expression with the `gi` flags, which stands for "global" and "case insensitive". The `g` flag ensures all occurrences of the pattern are replaced, and the `i` flag makes the matching case-insensitive.

I hope this helps! Let me know if you have any more questions.
```

```javascript
function removeVowels(text) {
  const vowels = ["a", "e", "i", "o", "u"];
  return text.replace(/[aeiou]/gi, '');
}
```

This function defines a variable `vowels` that holds an array of vowel characters. It then uses the `replace` method on the `text` parameter, passing a regular expression `/[aeiou]/gi` as the first argument and an empty string `''` as the second argument.

The regular expression `/[aeiou]/gi` matches any character