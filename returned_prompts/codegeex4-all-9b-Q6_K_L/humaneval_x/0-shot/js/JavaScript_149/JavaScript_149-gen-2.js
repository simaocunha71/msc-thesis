```javascript
const sortedListSum = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    sum += parseInt(lst[i]);
  }
  return sum;
}
```
