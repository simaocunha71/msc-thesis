You can use the `map` function to increment each element in the list by 1. Here's a possible solution:

```javascript
const incrList = (l) => {
  return l.map(x => x + 1);
}
```

This solution uses the `map` function to iterate over each element in the list `l` and creates a new list with each element incremented by 1.