You can solve this by using the `Math.ceil()` function to round each element in the list to the upper int(Ceiling) first, then use the `map()` function to square each element, and finally use the `reduce()` function to sum all the squared elements. Here is the complete solution:

```javascript
const sumSquares = (lst) => {
  return lst.map(Math.ceil).map(x => x * x).reduce((a, b) => a + b, 0);
}
```

In this solution, `lst.map(Math.ceil)` rounds each element in the list to the upper int(Ceiling), `lst.map(x => x * x)` squares each element, and `lst.reduce((a, b) => a + b, 0)` sums all the squared elements. The `0` is the initial value of the reduce function.