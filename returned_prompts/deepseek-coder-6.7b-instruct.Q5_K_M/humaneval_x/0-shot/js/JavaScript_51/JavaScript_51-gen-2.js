  return text.replace(/[aeiou]/gi, '');

};

module.exports = removeVowels;
```

This code defines a function `removeVowels` that takes a string `text` as an argument. The function uses the `replace` method of the String object to replace all occurrences of the vowels in the string with an empty string. The `/[aeiou]/gi` regular expression matches any vowel in the string, and the `i` flag makes the match case insensitive. The function then returns the modified string.

It's a great example of using the power of regular expressions in JavaScript to perform string manipulation.

Here's the test cases you can use to validate your solution:

```javascript
console.log(removeVowels('')); // ''
console.log(removeVowels('abcdef\nghijklm')); // 'bcdf\nghjklm'
console.log(removeVowels('abcdef')); // 'bcdf'
console.log(removeVowels('aaaaa')); // ''
console.log(removeVowels('aaBAA')); // 'B'
console.log(removeVowels('zbcd')); // 'zbcd'
```

This code should pass all of these test cases.

Please note that this code will remove both uppercase and lowercase vowels.

Let's test it:

```javascript
console.log(removeVowels('Hello World')); // 'Hll Wrld'
console.log(removeVowels('AEIOU')); // ''
console.log(removeVowels('aeiou')); // ''
console.log(removeVowels('bcdfghjklmnpqrstvwxyz')); // 'bcdfghjklmnpqrstvwxyz'
```

All the vowels have been removed from the string.

In this solution, we used the `replace` method of the string object with a regular expression to remove all the vowels from a string. The `/[aeiou]/gi` regular expression matches all vowels in the string, and the `replace` method replaces them with an empty string. The `g`