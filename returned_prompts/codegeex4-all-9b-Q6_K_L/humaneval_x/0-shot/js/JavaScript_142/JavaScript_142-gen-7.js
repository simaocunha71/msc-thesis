```javascript
const sumSquares = (lst) => {
  return lst.reduce((acc, num, i) => {
    if (i % 3 === 0) acc += num * num;
    if (i % 4 === 0 && i % 3 !== 0) acc += num * num * num;
    if (i % 3 !== 0 && i % 4 !== 0) acc += num;
    return acc;
  }, 0);
}
```