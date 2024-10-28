```javascript
function roundedAvg(n, m) {
  if (n > m) {
    return -1;
  }
  const sum = (n + m) * (m - n + 1) / 2;
  const avg = Math.round(sum / (m - n + 1));
  return avg.toString(2);
}
```


Explanation:
1. Check if n is greater than m, if yes return -1.
2. Calculate the sum of the integers from n to m using the formula for the sum of an arithmetic series: (n + m) * (m - n + 1) / 2.
3. Calculate the average by dividing the sum by the number of integers (m - n + 1).
4. Round the average to the nearest integer using the Math.round() function.
5. Convert the rounded average to binary using the toString() function with the base 2 argument (2).

Note: The binary representation is obtained by converting the integer to a string using the toString() function with the base 2 argument (2). This will give the binary representation of the integer. For example, the decimal number 5 will be represented as "0b101" in binary.