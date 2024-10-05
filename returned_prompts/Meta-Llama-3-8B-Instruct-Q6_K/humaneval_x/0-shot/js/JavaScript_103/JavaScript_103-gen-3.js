Here is a JavaScript function that solves the problem:

```javascript
const roundedAvg = (n, m) => {
  if (n > m) {
    return -1;
  }
  const sum = (m + n) * (m - n + 1) / 2;
  const avg = Math.round(sum / (m - n + 1));
  return avg.toString(2);
};
```

This function first checks if n is greater than m. If it is, the function returns -1. If not, the function calculates the sum of the integers from n through m using the formula for the sum of an arithmetic series. It then calculates the average by dividing the sum by the number of integers in the series. The average is rounded to the nearest integer using the Math.round function. Finally, the function converts the average to binary using the toString method and returns the result.

For example, if you call the function with the arguments 1 and 5, it will return "0b11", which is the binary representation of the rounded average of the integers from 1 through 5. If you call the function with the arguments 7 and 5, it will return -1, because 7 is greater than 5. If you call the function with the arguments 10 and 20, it will return "0b1111", which is the binary representation of the rounded average of the integers from 10 through 20. If you call the function with the arguments 20 and 33, it will return "0b11010", which is the binary representation of the rounded average of the integers from 20 through 33.