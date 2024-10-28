You can use the Math.ceil() function to round each element in the list to the upper int(Ceiling) first. Then, you can use the map() function to square each element in the new list and finally use the reduce() function to sum the squared elements.
Here is the implementation in JavaScript:

```javascript
const sumSquares = (lst) => {
  let ceilList = lst.map(num => Math.ceil(num));
  let squaredList = ceilList.map(num => num * num);
  return squaredList.reduce((acc, cur) => acc + cur, 0);
}
```

In the above code:
- lst.map(num => Math.ceil(num)) rounds each element in the list to the upper int(Ceiling) first.
- squaredList.map(num => num * num) squares each element in the new list.
- squaredList.reduce((acc, cur) => acc + cur, 0) sums the squared elements.