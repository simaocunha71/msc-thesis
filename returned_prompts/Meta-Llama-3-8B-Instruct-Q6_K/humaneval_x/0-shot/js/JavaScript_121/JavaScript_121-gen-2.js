```javascript
const solution = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 2 === 0 && lst[i] % 2 !== 0) {
      sum += lst[i];
    }
  }
  return sum;
};
```


Explanation:
This function iterates over the input list, checking if the current index is even (i % 2 === 0) and if the current element is odd (lst[i] % 2 !== 0). If both conditions are true, it adds the element to the sum. The function finally returns the sum of all the odd elements in even positions.