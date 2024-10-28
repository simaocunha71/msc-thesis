Here is one possible solution. The function `countNums` takes an array of integers as an argument and returns the number of elements that have a sum of digits greater than 0. 

To achieve this, we can follow these steps:

1. Define a helper function called `sumOfDigits` that takes a number as an argument and returns the sum of its digits. If the number is negative, the function will convert the number to its absolute value and then calculate the sum of digits. If the number is positive, it will calculate the sum of digits directly.

2. Define the `countNums` function and initialize a counter variable to keep track of the number of elements with a sum of digits greater than 0.

3. Iterate through each element in the input array using the `forEach` method. For each element, call the `sumOfDigits` function to calculate the sum of digits. If the sum of digits is greater than 0, increment the counter by 1.

4. After iterating through all the elements in the array, return the final value of the counter.

Here's the implementation of the solution:

```javascript
const countNums = (arr) => {
  let counter = 0;
  arr.forEach(num => {
    if (sumOfDigits(num) > 0) {
      counter++;
    }
  });
  return counter;
};

const sumOfDigits = (num) => {
  let absoluteNum = Math.abs(num);
  let digitsSum = 0;

  while (absoluteNum > 0) {
    digitsSum += absoluteNum % 10;
    absoluteNum = Math.floor(absoluteNum / 10);
  }

  return digitsSum;
};
```

By using the `sumOfDigits` helper function, we can calculate the sum of digits for each number in the array and determine if it is greater than 0. If it is, we increment the counter. Finally, we return the counter, which represents the number of elements with a sum of digits greater than 0 in the input array.

You can test the `countNums` function with the provided test cases to verify its correctness:
