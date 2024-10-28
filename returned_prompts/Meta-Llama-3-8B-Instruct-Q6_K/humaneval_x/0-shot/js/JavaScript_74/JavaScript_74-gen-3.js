Here is the solution in JavaScript:

```javascript
const totalMatch = (lst1, lst2) => {
  let sum1 = 0;
  let sum2 = 0;

  lst1.forEach(str => {
    sum1 += str.length;
  });

  lst2.forEach(str => {
    sum2 += str.length;
  });

  if (sum1 < sum2) {
    return lst1;
  } else if (sum1 > sum2) {
    return lst2;
  } else {
    return lst1;
  }
};
```
This function iterates over each list of strings, summing up the length of each string. It then compares these sums to determine which list has the total number of characters less than the other. If the sums are equal, it returns the first list. If the sums are not equal, it returns the list with the smaller sum.