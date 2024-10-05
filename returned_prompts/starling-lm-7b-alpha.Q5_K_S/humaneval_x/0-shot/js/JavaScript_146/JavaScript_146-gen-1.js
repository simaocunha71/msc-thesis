To solve this problem, you can follow these steps:

1. Initialize a variable `count` to keep track of the number of elements that are greater than 10 and have both first and last digits as odd. Initialize it to 0.
2. Iterate through each element `num` in the `nums` array using a `for...of` loop.
3. Inside the loop, check if the number is greater than 10 and if both the first and last digits are odd. You can use the modulo operator (`%`) to check if a number is odd. The first digit can be obtained by dividing the number by 10 and taking the remainder, and the last digit can be obtained by taking the remainder of the number divided by 10.
4. If both conditions are met, increment the `count` variable by 1.
5. After iterating through all the elements in the `nums` array, return the value of the `count` variable as the result.
6. The function should return the number of elements in the `nums` array that satisfy the conditions.

Here's the code for the `specialFilter` function that implements the above steps:

```javascript
const specialFilter = (nums) => {
  let count = 0;
  for (const num of nums) {
    if (num > 10 && (num % 10) % 2 === 1 && Math.floor(num / 10) % 10 % 2 === 1) {
      count++;
    }
  }
  return count;
};
```

You can test the function with the provided examples:

```javascript
console.log(specialFilter([15, -73, 14, -15])); // Output: 1
console.log(specialFilter([33, -2, -3, 45, 21, 109])); // Output: 2
```

The `specialFilter` function will return the number of elements in the array that meet the conditions (greater than 10 and both first and last digits are odd).

*/

const specialFilter = (nums) => {
  let count = 0;
  for (const num