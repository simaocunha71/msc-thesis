```javascript
const sumSquares = (lst) => {
  return lst.reduce((sum, num, idx) => {
    if (idx % 3 === 0) sum += num * num;
    if (idx % 4 === 0 && idx % 3 !== 0) sum += num * num * num;
    return sum;
  }, 0);
}
```
