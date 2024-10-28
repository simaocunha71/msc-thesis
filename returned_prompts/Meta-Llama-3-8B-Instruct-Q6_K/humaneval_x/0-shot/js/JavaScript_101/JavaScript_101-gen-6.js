The function `wordsString` takes a string as input and returns an array of words. The string is split into words using the `split` method with a regular expression that matches one or more commas or spaces. The resulting array of words is then returned.

Here is the solution:
```
const wordsString = (s) => {
  return s.split(/[\s,]+/)
}
```
This regular expression `[\s,]+` matches one or more occurrences of either a whitespace character (`\s`) or a comma (`,`). The `split` method splits the input string into an array of substrings at each occurrence of this pattern.

For example, if the input string is `"Hi, my name is John"`, the regular expression will match the commas and spaces, and the resulting array of words will be `["Hi", "my", "name", "is", "John"]`. Similarly, if the input string is `"One, two, three, four, five, six"`, the regular expression will match the commas and spaces, and the resulting array of words will be `["One", "two", "three", "four", "five", "six"]`.