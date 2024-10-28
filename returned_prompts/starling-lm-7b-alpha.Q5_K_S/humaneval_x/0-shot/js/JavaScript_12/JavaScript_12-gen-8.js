To solve this problem, you can use the `reduce` method in JavaScript to find the longest string in the array. Here's an example implementation:

```javascript
const longest = (strings) => {
  return strings.reduce((longest, current) => {
    if (current.length > longest.length) {
      return current;
    } else {
      return longest;
    }
  });
};
```

