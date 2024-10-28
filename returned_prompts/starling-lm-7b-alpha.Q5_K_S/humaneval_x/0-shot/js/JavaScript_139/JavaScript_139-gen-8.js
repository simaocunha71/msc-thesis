
    if (n <= 1) {
        return 1;
    }

    return n * specialFactorial(n - 1);
};

console.log(specialFactorial(4));



*/







/*

To calculate the Brazilian factorial, you multiply each integer from the original integer to 1. For example, the Brazilian factorial of 5 is calculated as follows:

5 * 4 * 3 * 2 * 1

The Brazilian factorial of an integer n is calculated in a similar manner:

n * (n - 1) * (n - 2) * ... * 1

To calculate the Brazilian factorial of an integer n, you can create a function called specialFactorial that takes an integer as an argument and returns the Brazilian factorial of that integer. Here's a step-by-step guide on how to create this function:

1. Define the specialFactorial function that takes an integer n as an argument.
2. Check if the input value of n is less than or equal to 1. If it is, return 1, as the factorial of 0 and 1 is always 1.
3. If the input value of n is greater than 1, call the specialFactorial function recursively with the argument n - 1, and multiply the result by n.
4. Repeat step 3 until the value of n is reduced to 1.
5. Return the final result.

For example, if you call specialFactorial(4), the function will return 24, which is the Brazilian factorial of 4.

*/






































































































































