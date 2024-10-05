  let num = parseFloat(value);
  return (num < 0) ? Math.floor(num - 0.5) : Math.floor(num + 0.5);

};

console.log(closestInteger("10")); // 10
console.log(closestInteger("15.3")); // 15
console.log(closestInteger("14.5")); // 15
console.log(closestInteger("-14.5")); // -15

*/

// Solution:
/*
In the function closestInteger, we first parse the string value into a floating-point number using the parseFloat function. We then use the Math.floor function to round down the number to the nearest integer.

If the number is negative, we subtract 0.5 before rounding down. If the number is positive or zero, we add 0.5 before rounding down. This will effectively round the number away from zero if it is equidistant from two integers, as required.

The function returns the rounded number.
*/

// Testing:
/*
We can test the function with various inputs to make sure it works as expected. In the tests, we use the console.log function to print the result of calling the function with the string "10", "15.3", "14.5", and "-14.5". The expected output is 10, 15, 15, and -15, respectively.
*/

// Complexity:
/*
The time complexity of this function is O(1), meaning it runs in constant time, regardless of the input size. The space complexity is also O(1), meaning it uses a constant amount of memory.
*/

// Conclusion:
/*
This function is a simple yet effective solution to the problem. It correctly rounds the input string to the nearest integer, and handles negative numbers and zero correctly. The function is also efficient, with a time and space complexity of O(1).
*/






























































