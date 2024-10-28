The solution is to convert the array to a Set, which automatically removes duplicates, and then convert it back to an array and sort it. Here is the code:

```javascript
const unique = (l) => {
  return [...new Set(l)].sort((a, b) => a - b);
}
```

In the code above, the spread operator (`...`) is used to convert the Set back into an array. The `sort()` function is used to sort the array in ascending order. The comparison function `(a, b) => a - b` is used to sort the array numerically, as by default the `sort()` function sorts elements as strings.