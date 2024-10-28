```
const wordsString = (s) => {
  return s.split(/[ ,]+/);
};
```


Explanation:
The problem requires you to split a given string into words and return an array of the words. The string is separated by commas or spaces. 

The solution uses the `split()` method, which splits a string into an array of strings. The argument to `split()` is a regular expression that matches the characters that separate the words. In this case, we use `[ ,]+`, which matches one or more spaces or commas.

Here's how it works:

- `s.split()` splits the input string `s` into an array of strings.
- `[ ,]+` is the regular expression that matches one or more spaces or commas. The square brackets `[]` create a character class that matches any of the characters inside. The comma `,` is escaped with a backslash `\` because it has a special meaning in regex. The `+` quantifier after the character class means "one or more of the preceding element".
- The resulting array of strings is then returned by the function `wordsString()`. 

For example, if you call `wordsString("Hi, my name is John")`, the function will split the string into an array `["Hi", "my", "name", "is", "John"]`. If you call `wordsString("One, two, three, four, five, six")`, the function will split the string into an array `["One", "two", "three", "four", "five", "six"]`. 

This solution is concise, efficient, and easy to understand, making it a good choice for solving this problem.