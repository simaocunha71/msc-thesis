You can use the `reduce()` method to find the longest string in the list. Here is the implementation:

```javascript
const longest = (strings) => {
  if (strings.length === 0) return null;
  return strings.reduce((a, b) => a.length >= b.length ? a : b);
}
```

In the above code, `reduce()` iterates through the array and returns the longest string. If the input list is empty, it returns `null`.