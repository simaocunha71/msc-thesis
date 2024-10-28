You can use regular expressions to solve this problem. Here's how:

```javascript
const isBored = (S) => {
  const regex = /I[^.!?]*[.!?]/g;
  return (S.match(regex) || []).length;
}
```

This regular expression `/I[^.!?]*[.!?]/g` matches any substring that starts with 'I' and is followed by any number of characters that are not '.', '?', or '!', and ends with '.', '?', or '!'. The `g` flag means that it will match all occurrences in the string, not just the first one.

The `match()` method returns an array of all matches found in the string. If no matches are found, it returns `null`. We use the `|| []` part to ensure that we always return an array, even if there are no matches. Finally, we return the length of this array, which is the number of boredoms.