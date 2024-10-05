  const lastDigit = (n) => Math.abs(n % 10);
  return lastDigit(a) * lastDigit(b);
}
console.log(multiply(148, 412)); // 16
console.log(multiply(19, 28)); // 72
console.log(multiply(2020, 1851)); // 0
console.log(multiply(14,-15)); // 20

// Solution
// The function takes in two integers, a and b. It uses the JavaScript modulo operator to find the last digit of each number. It multiplies these last digits together and returns the result.

// The last digit of a number n is the remainder when n is divided by 10. For example, the last digit of 148 is 8 (148 % 10 = 8), the last digit of -15 is 5 (-15 % 10 = 5), and so on. The modulo operator automatically takes care of negative numbers by taking their absolute value.

// The multiply function is a one-line arrow function that uses the JavaScript arrow function syntax. It takes in two parameters, a and b, and returns the product of the last digits of a and b. It does this by calling the lastDigit function on a and b and then multiplying the results together.

// The console.log statements at the end are used to test the multiply function with the provided examples.

// The function should work for any two integers. It does not need any error checking or special handling for negative numbers or zero.

// If you want to test the function with other examples, you can add more console.log statements like the ones I did at the end of the code.





































































































