```
const antiShuffle = (s) => {
  return s.replace(/\b\w+\b/g, word => {
    return word.split('').sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('');
  });
};
```


Explanation:
The function uses the `replace` method with a regular expression to replace each word in the string with a new word where the characters are sorted in ascending order based on their ASCII values.

The regular expression `\b\w+\b` matches each word in the string, where `\b` is a word boundary and `\w+` matches one or more word characters (letters, numbers, underscores).

The replacement function `word => ...` takes each word as an argument, splits it into an array of characters using `split('')`, sorts the array using `sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0))`, and then joins the sorted array back into a string using `join('')`.

The `replace` method replaces each word in the original string with the sorted word, preserving the order of words and blank spaces in the sentence. The resulting string is returned by the `antiShuffle` function.