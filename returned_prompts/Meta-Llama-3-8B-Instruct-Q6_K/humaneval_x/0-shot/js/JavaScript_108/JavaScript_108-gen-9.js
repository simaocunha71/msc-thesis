Here is a JavaScript function that solves the problem:

```javascript
const countNums = (arr) => {
  let count = 0;
  for (let num of arr) {
    let sum = 0;
    let sign = 1;
    if (num < 0) {
      sign = -1;
      num = -num;
    }
    while (num > 0) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }
    if (sum > 0) {
      count++;
    }
  }
  return count;
};
```

This function iterates over each element in the input array. For each element, it calculates the sum of its digits by repeatedly taking the remainder of the number when divided by 10 (which gives the last digit), adding that digit to the sum, and then integer-dividing the number by 10 (which effectively removes the last digit). If the number is negative, it first makes it positive and then keeps track of the sign separately. If the sum of the digits is greater than 0, it increments the count. Finally, it returns the count.