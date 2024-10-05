Here is a simple function that accomplishes the task:

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
  } else if (sum2 < sum1) {
    return lst2;
  } else {
    return lst1;
  }
};
```

This function iterates through each list, calculating the total number of characters in each string. It then compares these sums, returning the list with the smaller sum. If the sums are equal, it returns the first list. This function assumes that the input lists only contain strings and does not check for this. If the input lists can contain non-string elements, you may want to add error checking code.