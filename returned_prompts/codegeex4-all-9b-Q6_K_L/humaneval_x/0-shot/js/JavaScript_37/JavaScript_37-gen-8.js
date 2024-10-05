```javascript
const sortEven = (l) => {
  let evenIndicies = [];
  let oddIndicies = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 2 === 0) {
      evenIndicies.push(l[i]);
    } else {
      oddIndicies.push(l[i]);
    }
  }
  evenIndicies.sort((a, b) => a - b);
  let sortedList = [];
  for (let i = 0; i < evenIndicies.length; i++) {
    sortedList.push(evenIndicies[i]);
    sortedList.push(oddIndicies[i]);
  }
  return sortedList;
}
```
