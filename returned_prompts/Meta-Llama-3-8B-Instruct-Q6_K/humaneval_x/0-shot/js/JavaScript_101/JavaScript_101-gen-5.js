```
const wordsString = (s) => {
  return s.replace(/,| /g, ' ').trim().split(' ');
};
```


Explanation:

The function `wordsString` takes a string `s` as input and returns an array of words.

1. `s.replace(/,| /g, ' ')`: This regular expression replaces all commas (`,`) and spaces (` `) with a single space (` `). This is done to ensure that the words are separated by a single space, which is easier to split.
2. `trim()`: This method removes any leading or trailing whitespace from the string.
3. `split(' ')`: This method splits the string into an array of words, using the space character as the separator.

For example, if the input string is `"Hi, my name is John"`, the function would first replace the commas and spaces with a single space, resulting in the string `"Hi my name is John"`. Then, it would trim the string to remove the leading and trailing spaces, resulting in the string `"Hi my name is John"`. Finally, it would split the string into an array of words, resulting in the array `["Hi", "my", "name", "is", "John"]`.