The solution is to map through the list, round each element to the upper int(Ceiling) first, then square the element and return the sum of the squared elements.

```javascript
const sumSquares = (lst) => {
  return lst.map(Math.ceil).map(x => x * x).reduce((a, b) => a + b, 0);
}
```

This solution works by first mapping through the list and applying `Math.ceil` to each element, then mapping through the list again and squaring each element, then finally reducing the list to a sum.