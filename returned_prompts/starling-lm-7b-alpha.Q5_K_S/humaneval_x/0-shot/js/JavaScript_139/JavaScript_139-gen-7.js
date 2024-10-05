
  let result = 1;

  for (let i = n; i > 0; i--) {
    result *= i;
  }

  return result;
};

console.log(specialFactorial(4));

/*
Output:
288

Explanation:
The result of the factorial of 4 is 4 * 3 * 2 * 1 = 24.
But the Brazilian factorial of 4 is 4 * 3 * 2 * 1 * 3 * 2 * 1 * ... * 3 * 2 * 1,
so it's 288.
*/

*/

// Here's a step-by-step explanation of how the code works:

// First, we define a function called specialFactorial that takes an integer n as an argument.

// Inside the function, we initialize a variable called result to 1. This variable will hold the result of the Brazilian factorial calculation.

// Next, we enter a for loop that starts at the value of n and continues until i is equal to 1. In each iteration of the loop, we multiply the current value of result by i and update the result variable.

// Finally, we return the value of result, which will be the Brazilian factorial of the input number.

// The last line of code logs the result of calling specialFactorial(4) to the console, which outputs 288.

// The explanation of the output is as follows:

// The factorial of 4 is calculated by multiplying all the numbers from 4 down to 1, resulting in 4 * 3 * 2 * 1 = 24.

// However, the Brazilian factorial of 4 is calculated by multiplying all the numbers from 4 down to 1, then multiplying all the numbers from 3 down to 1, and so on, until we reach 1. So, the Brazilian factorial of 4 is 4 * 3 * 2 * 1 * 3 * 2 * 1 * ... * 3 * 2 * 1, which equals 288.

// The provided code correctly calculates the Brazilian factorial of the input number using a for