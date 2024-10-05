    return Math.log2(x) % Math.log2(n) === 0;
};

console.log(isSimplePower(1, 4)); // true
console.log(isSimplePower(2, 2)); // true
console.log(isSimplePower(8, 2)); // true
console.log(isSimplePower(3, 2)); // false
console.log(isSimplePower(3, 1)); // false
console.log(isSimplePower(5, 3)); // false

*/

/*

In this code, we're using the Math.log2() method to calculate the logarithm base 2 of the given number x. This will give us the number of times 2 can be multiplied together to reach x. 

Then, we're using the modulo operator (%) to check if the result of the logarithm is divisible by the logarithm of the base number n. If they are divisible, it means that x is a simple power of n.

Finally, we're returning the result of the modulo operation, which will be true if x is a simple power of n, and false otherwise.

For example, when we call isSimplePower(1, 4), the logarithm of 1 is 0, and 0 modulo 2 is 0. So, the result is true.

When we call isSimplePower(2, 2), the logarithm of 2 is 1, and 1 modulo 2 is 1. So, the result is true.

When we call isSimplePower(8, 2), the logarithm of 8 is 3, and 3 modulo 2 is 1. So, the result is true.

When we call isSimplePower(3, 2), the logarithm of 3 is approximately 1.58, and 1.58 modulo 2 is 0.58. Since 0.58 is not equal to 0, the result is false.

When we call isSimplePower(3, 1), the logarithm of 3 is approximately 1.58, and 1.58 modulo 1 is 0.58. Since 0