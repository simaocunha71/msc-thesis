  return text.replace(/[aeiou]/gi, '');

}

console.log(removeVowels(''))
console.log(removeVowels("abcdef\nghijklm"))
console.log(removeVowels('abcdef'))
console.log(removeVowels('aaaaa'))
console.log(removeVowels('aaBAA'))
console.log(removeVowels('zbcd'))
```

This function uses the `replace()` method with a regular expression to match all vowels (both uppercase and lowercase, due to the `i` flag) and replaces them with an empty string.

Note: The `\n` is a newline character. This is also matched by the regular expression, so it will also be removed from the string.

## 2.3.11

```javascript
