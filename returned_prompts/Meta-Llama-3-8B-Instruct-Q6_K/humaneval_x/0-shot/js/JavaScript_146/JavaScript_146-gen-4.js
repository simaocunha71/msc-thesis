Here is the solution to the problem:

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

Explanation:

* We initialize a variable `count` to 0, which will be used to keep track of the number of elements in the array that satisfy the conditions.
* We use a `for...of` loop to iterate over each element in the input array `nums`.
* For each element, we check if it satisfies the two conditions:
  1. `Math.abs(num) > 10`: This checks if the absolute value of the number is greater than 10.
  2. `num % 10 % 2 !== 0 && Math.floor(Math.abs(num) / 10) % 2 !== 0`: This checks if both the last digit and the first digit of the number are odd. We use the modulo operator `%` to check if a number is odd, and `Math.floor` to get the first digit of the number.
* If an element satisfies both conditions, we increment the `count` variable.
* Finally, we return the `count` variable, which represents the number of elements in the array that satisfy the conditions.