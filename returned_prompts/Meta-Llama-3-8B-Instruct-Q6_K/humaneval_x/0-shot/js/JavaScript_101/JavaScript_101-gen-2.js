Here is a simple JavaScript function that does the task:

```javascript
const wordsString = (s) => {
  return s.split(/[\s,]+/);
};
```

In this function, the `split()` method is used to split the input string `s` into an array of words. The regular expression `/[\s,]+/` matches one or more whitespace characters (spaces or commas). This regular expression is used as the separator for the `split()` method.

You can test the function with the examples you provided:

```javascript
console.log(wordsString("Hi, my name is John")); // Output: ["Hi", "my", "name", "is", "John"]
console.log(wordsString("One, two, three, four, five, six")); // Output: ["One", "two", "three", "four", "five", "six"]
```



This function works by splitting the input string `s` into an array of words, using the regular expression `/[\s,]+/` as the separator. The `split()` method splits the string at each occurrence of the separator, and returns an array of the resulting substrings.

The regular expression `/[\s,]+/` matches one or more whitespace characters (spaces or commas). The `[` and `]` characters are used to specify a character class, which matches any of the characters within the class. The `\s` matches a whitespace character (space, tab, newline, etc.), and the `,` matches a comma. The `+` character after the character class specifies that the preceding pattern should be matched one or more times.

By using this regular expression as the separator for the `split()` method, the function is able to split the input string into an array of words, regardless of whether the words are separated by spaces or commas.