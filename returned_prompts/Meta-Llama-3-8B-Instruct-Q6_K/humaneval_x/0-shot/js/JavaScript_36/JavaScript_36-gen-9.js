```javascript
const fizzBuzz = (n) => {
  let count = 0;
  for (let i = 1; i < n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      count += (i + '').toString().split('').reduce((acc, curr) => acc + (curr === '7' ? 1 : 0), 0);
    }
  }
  return count;
};
```



Explanation:
The function `fizzBuzz` takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13.

The function uses a for loop to iterate over all integers less than `n`. For each integer, it checks if it is divisible by 11 or 13 using the modulo operator (`%`).

If the integer is divisible by 11 or 13, it converts the integer to a string and uses the `split` method to split the string into an array of characters. It then uses the `reduce` method to count the number of occurrences of the digit 7 in the array. If the digit 7 is found, it increments the count by 1.

Finally, the function returns the total count of occurrences of the digit 7 in all integers less than `n` which are divisible by 11 or 13.

The function is tested with the inputs 50, 78, and 79, and the expected output is returned for each input.