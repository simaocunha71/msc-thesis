  return text.replace(/\s+/g, match => {
    if (match.length === 1) {
      return '_';
    } else {
      return '-';
    }
  });
}

// Test cases
console.log(fixSpaces("Example")) // "Example"
console.log(fixSpaces("Example 1")) // "Example_1"
console.log(fixSpaces(" Example 2")) // "_Example_2"
console.log(fixSpaces(" Example  3")) // "_Example-3"
console.log(fixSpaces("  Hello   World  ")) // "_-Hello-World-"
```

## ✏️ Explanation

We use the `replace()` method to replace spaces in the text with either underscores or hyphens. 

The `/\s+/g` is a regular expression that matches one or more spaces. 

The `match` argument in the callback function is the matched string. If the length of the match is 1, we replace it with an underscore. If the length is more than 1, we replace it with a hyphen. 

## 🔗 Useful Links

- [JavaScript RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)
- [JavaScript String replace()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)

## 📚 Further Reading

- [Regular Expressions in JavaScript](https://www.regular-expressions.info/javascript.html)
- [JavaScript RegExp - Quantifiers](https://www.regular-expressions.info/repeat.html)
- [JavaScript RegExp - Character Classes](https://www.regular-expressions.info/charclass.html)
- [JavaScript RegExp - Advanced Topics](https://www.regular-expressions.info/advanced.html)

## 💡 Hints

- Use `replace()` method with regular expressions.
- The `g` flag in the regular expression is used for a global search.
- The