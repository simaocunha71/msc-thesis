You can increment each element in a list using a map function. Here's how you can do it in JavaScript:

```javascript
const incrList = (l) => {
  return l.map(x => x + 1);
}
```

This code uses the `map` function to iterate over each element in the list `l`, and adds 1 to each element. The result is a new list with all elements incremented by 1.