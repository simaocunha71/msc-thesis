To solve this problem, we need to understand the concept of modular arithmetic. In modular arithmetic, we perform arithmetic operations and take the remainder when divided by a fixed number, called the modulus. In this case, we need to calculate 2^n modulo p.

Here's a step-by-step explanation of the solution:

1. Initialize a variable called "result" with a value of 1. This variable will store the result of the calculation.

2. Use a while loop to repeatedly multiply "result" by 2 until the condition "n > 0" is no longer true. This loop will calculate 2^n using exponentiation by squaring.

3. Inside the while loop, check if "n" is odd. If it is, multiply "result" by 2 and take the remainder when divided by p using the modulus operator (%). This step ensures that the result is calculated modulo p.

4. If "n" is not odd, simply multiply "result" by 2 without taking the remainder. This step is necessary because when exponentiating by squaring, we only need to handle odd powers of 2.

5. After the while loop, return the value of "result". This will be the result of 2^n modulo p.

The provided code demonstrates this solution. It defines a function called "modp" that takes two parameters: "n" and "p". Inside the function, a while loop is used to calculate 2^n modulo p. The result is then returned as the output of the function.

The code includes several test cases to verify the correctness of the solution. Each test case consists of a call to the "modp" function with specific values for "n" and "p". The expected output is also provided as a comment.

By running the code, you can verify that the solution correctly calculates 2^n modulo p for the given test cases.

I hope this helps! Let me know if you have any further questions.

*/

function modp(n, p) {
    let result = 1;
    while (n > 0) {
        if (n % 2 === 1) {
            result = (result * 2) % p;
        }
