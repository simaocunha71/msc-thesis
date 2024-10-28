Here is the solution using JavaScript:

```javascript
const search = (lst) => {
  let max = -1;
  for (let num of lst) {
    if (num > 0 && lst.filter(x => x === num).length >= num) {
      max = Math.max(max, num);
    }
  }
  return max === -1 ? -1 : max;
};
```

This function iterates over the list, checks if the number is greater than 0 and its frequency is greater than or equal to the number itself, and updates the maximum value if necessary. If no such value is found, it returns -1. The function uses the `filter` method to count the frequency of each number. If the maximum value is still -1 after iterating over the entire list, it means no such value was found, so the function returns -1. Otherwise, it returns the maximum value.