To determine if a number is prime, we need to check if it is divisible by any number from 2 to n-1. If it is divisible by any of these numbers, then it is not prime. Otherwise, it is prime.

We can use a loop to iterate through the range of 2 to n-1 and check if the number is divisible by any of these numbers. If it is divisible by any number, we return false, indicating that the number is not prime. If the loop completes without finding a divisor, we return true, indicating that the number is prime.

In the provided solution, the `isPrime` function takes a number `n` as an input and checks if it is divisible by any number from 2 to n-1 using a for loop. The loop iterates through each number in the range and checks if `n` is divisible by it using the modulo operator (`%`). If the remainder is 0, it means that `n` is divisible by the current number, and the function returns false. If the loop completes without finding a divisor, the function returns true, indicating that the number is prime.

For example, when we call `isPrime(6)`, the function checks if 6 is divisible by 2, 3, 4, and 5. Since 6 is divisible by 2, the function returns false, indicating that 6 is not a prime number. Similarly, when we call `isPrime(101)`, the function checks if 101 is divisible by any number from 2 to 100. Since it is not divisible by any of these numbers, the function returns true, indicating that 101 is a prime number.

You can use this `isPrime` function to check if any given number is prime or not.

Here's an example usage of the function:
```
console.log(isPrime(6));     // false
console.log(isPrime(101));   // true
console.log(isPrime(11));    // true
console.log(isPrime(13441)); // true
console.log(isPrime(61));    // true
console.log(isPrime(4));     //