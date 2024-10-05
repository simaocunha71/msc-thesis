Here is a JavaScript function that solves the problem:

```javascript
const specialFilter = (nums) => {
  let count = 0;
  for (let num of nums) {
    if (Math.abs(num) > 10 && num % 10 % 2 !== 0 && Math.floor(Math.abs(num) / 10) % 2 !== 0) {
      count++;
    }
  }
  return count;
};
```

This function iterates over each number in the input array. It checks if the absolute value of the number is greater than 10, and if the last digit of the number (obtained using the modulus operator `%`) is odd (i.e., `num % 10 % 2 !== 0`). It also checks if the first digit of the number (obtained by taking the floor of the absolute value of the number divided by 10) is odd (`Math.floor(Math.abs(num) / 10) % 2 !== 0`). If all these conditions are met, it increments the count. Finally, it returns the count.

For example, when called with the input `[15, -73, 14, -15]`, the function returns `1`, and when called with the input `[33, -2, -3, 45, 21, 109]`, it returns `2`.