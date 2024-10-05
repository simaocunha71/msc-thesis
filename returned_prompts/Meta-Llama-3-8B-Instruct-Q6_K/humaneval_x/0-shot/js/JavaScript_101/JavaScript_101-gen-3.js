```
const wordsString = (s) => s.split(/[ ,]+/g);
```

Explanation:
The `split()` method is used to split the string into an array of words. The regular expression `/[ ,]+/g` is used as the separator. This regular expression matches one or more spaces or commas.

The `g` flag at the end of the regular expression makes the split method split the string globally, i.e., it will split the string into an array of words as many times as it finds the separator.

For example, `wordsString("Hi, my name is John")` will return `["Hi", "my", "name", "is", "John"]` and `wordsString("One, two, three, four, five, six")` will return `["One", "two", "three", "four", "five", "six"]`.