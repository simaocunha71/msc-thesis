To solve this problem, you can follow these steps:

1. Find the maximum number in the list.
2. Convert the maximum number to a string and split it into an array of digits.
3. Initialize a variable `sum` to 0 to store the sum of the digits.
4. Use a loop to iterate through each digit in the array and add its numeric value to the `sum` variable.
5. After calculating the sum of the digits, you need to find the largest prime number among all the numbers in the list. To do this, you can use the following steps:

   a. Start with the maximum number and check if it is divisible by any number between 2 and the square root of the maximum number (inclusive). If it is divisible, subtract 1 from the maximum number and break the loop. This step ensures that the maximum number is a prime number.
   
   b. If the maximum number is not divisible by any number between 2 and the square root of the maximum number, it is a prime number and you can use it for the final result.
   
6. Return the sum of the digits of the largest prime number.

Here's the code that implements the above steps:

```javascript
const skjkasdkd = (lst) => {
  let max = Math.max(...lst);
  let arr = max.toString().split("");
  let sum = 0;

  for(let i = 0; i < arr.length; i++) {
    sum += Number(arr[i]);
  }

  while(max > 1) {
    for(let i = 