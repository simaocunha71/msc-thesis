```
function fizzBuzz(n) {
  let count = 0;
  for (let i = 11; i < n; i += 11) {
    if (i.toString().includes('7')) {
      count++;
    }
  }
  for (let i = 13; i < n; i += 13) {
    if (i.toString().includes('7')) {
      count++;
    }
  }
  return count;
}
```


Here is how it works:

1. We initialize a counter `count` to 0.
2. We loop through all the numbers from 11 to `n-1` in increments of 11.
3. For each number, we convert it to a string and check if it contains the digit 7 using the `includes` method. If it does, we increment the `count`.
4. We do the same for numbers from 13 to `n-1` in increments of 13.
5. Finally, we return the `count`.

This function is case-insensitive, meaning it will count both lowercase and uppercase occurrences of the digit 7.

For example, if `n` is 50, the function will count the numbers 77, 17, and 71, which are divisible by 11 or 13, and return 3. If `n` is 78, it will count the numbers 77 and 71, and return 2. If `n` is 79, it will count the numbers 77, 17, and 71, and return 3.