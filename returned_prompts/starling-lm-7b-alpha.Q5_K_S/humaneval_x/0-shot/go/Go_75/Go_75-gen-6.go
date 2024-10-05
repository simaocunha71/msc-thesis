
Here's a step by step explanation of the solution:

1. We start by creating a boolean array of size 100. This array is used to mark the prime numbers.
2. The function `isPrime` is created to check if a number is prime. We will use this function later to check if a number is a prime number or not.
3. Now, we start by initializing the boolean array by marking all numbers from 0 to 99 as prime.
4. Then, we start a loop that will go from 2 to 99.
5. For every number from 2 to 99, we check if it’s prime or not using the `isPrime` function. If it is prime, we mark it as not prime in the boolean array.
6. After marking all the non-prime numbers, we start another loop to check if the given number `a` can be multiplied with 3 prime numbers.
7. We use the `isPrime` function to check if `a` is a prime number or not. If it is, we return false because prime numbers can’t be multiplied with 3 prime numbers to get `a`.
8. If `a` is not a prime number, we check if it can be divided by 3 and the other two prime numbers stored in the boolean array. If it can be divided, we return true, otherwise, we return false.
9. The `isPrime` function is defined as follows:
    - It takes an integer `n` as an argument.
    - It starts by checking if `n` is less than or equal to 1. If it is, it returns false because 1 and 0 are not prime numbers.
    - It then checks if `n` is equal to 2. If it is, it returns true because 2 is the only even prime number.
    - If `n` is greater than 2, it starts a loop to check if `n` can be divided by any number from 2 to sqrt(n). If it can be divided, it returns false because the number is not prime. If it can’t be divided, it returns true because the number is prime.

Here's the complete code:

```go
package main

import "fmt"

func isPr