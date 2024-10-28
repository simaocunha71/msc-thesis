To solve this problem, we need to iterate through all the numbers less than n and check if the number is divisible by 11 or 13. Then, we count the number of times the digit 7 appears in these numbers. Here's a step-by-step solution:

1. Initialize a variable called 'count' to store the number of times the digit 7 appears in the eligible numbers. Set it to 0 initially.
2. Use a for loop to iterate through all the numbers less than n.
3. Inside the loop, check if the current number is divisible by 11 or 13. If it is, proceed to step 4. Otherwise, skip to step 7.
4. Check if the current number contains the digit 7. If it does, increment the 'count' variable by 1.
5. Repeat steps 3-4 until all eligible numbers have been checked.
6. After the loop, return the final value of 'count'.
7. If the current number is not divisible by 11 or 13, move on to the next number and repeat steps 3-7.
8. Repeat steps 2-7 until all numbers less than n have been checked.

Here's an example implementation of the solution in JavaScript:

```javascript
const fizzBuzz = (n) => {
  let count = 0;
  for (let i = 1; i < n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      if (i.toString().includes('7')) {
        count++;
      }
    }
  }
  return count;
};
```

In this code, we use a for loop to iterate through all the numbers less than n. Inside the loop, we check if the current number is divisible by 11 or 13 using the modulo operator (%). If it is, we then check if the number contains the digit 7 by converting it to a string and using the includes() method. If the digit 7 is found, we increment the 'count' variable by 1. Finally, we return the value of 'count', which represents the number of times the digit 7 appears in the eligible numbers.

