Here's how you could solve this problem:

```javascript
const wordsString = (s) => {
  return s.split(/, | /);
};
```

In this solution, we use the `split()` method of JavaScript strings. This method splits a string into an array of substrings based on a specified separator. In this case, we use a regular expression that matches either a comma followed by a space (`', '`) or just a space (`' '`) as the separator. This will split the string into words wherever there's a comma followed by a space or just a space.