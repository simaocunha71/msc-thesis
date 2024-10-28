```javascript
const median = (l) => {
  var sortedL = l.sort((a, b) => a - b);
  var mid = Math.floor(sortedL.length / 2);
  if (sortedL.length % 2 === 0) {
    return (sortedL[mid - 1] + sortedL[mid]) / 2;
  } else {
    return sortedL[mid];
  }
}
```