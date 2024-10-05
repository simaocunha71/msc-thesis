You can use the `split()` method to split the string into words. This method splits a string into an array of strings by separating the string into substrings.

Here's how you can do it:

```javascript
const wordsString = (s) => {
  return s.split(/[\s,]+/);
};
```

The regular expression `/[\s,]+/` is used to match one or more spaces or commas. This regular expression will split the string at each space or comma.