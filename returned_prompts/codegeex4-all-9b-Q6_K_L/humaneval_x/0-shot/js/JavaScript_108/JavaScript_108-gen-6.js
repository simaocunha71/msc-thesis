Here's one possible implementation:

```javascript
const countNums = (arr) => {
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    let num = arr[i];
    let sum = 0;
    while (num !== 0) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }
    if (sum > 0) {
      count++;
    }
  }
  return count;
}
```

This function iterates through the array, calculates the sum of digits for each number, and increments the count if the sum is greater than 0.