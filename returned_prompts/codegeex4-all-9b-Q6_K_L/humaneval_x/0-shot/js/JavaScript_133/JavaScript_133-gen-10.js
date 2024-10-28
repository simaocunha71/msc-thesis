You can solve this problem by using the Math.ceil() function to round each element in the list to the upper int(Ceiling) first, then use the Array.prototype.map() function to square each element in the list, and finally use the Array.prototype.reduce() function to sum up the squared numbers in the list.

Here is a possible implementation:

```javascript
const sumSquares = (lst) => {
  return lst.map(Math.ceil).map(x => x * x).reduce((a, b) => a + b, 0);
};
```

This implementation first uses the Array.prototype.map() function to round each element in the list to the upper int(Ceiling) first, then uses the Array.prototype.map() function again to square each element in the list, and finally uses the Array.prototype.reduce() function to sum up the squared numbers in the list.