In this problem, we have to determine whether the given number is a product of exactly three prime numbers. The function isMultiplyPrime is the main function which takes a number as input. 

The given number is factored and the factors are pushed into an array. The condition checks that the length of the array is 3 (which are the factors) and that every factor is a prime number. If both conditions are met, the function returns true, otherwise it returns false.

The helper function isPrime is used to check if a number is prime. It iterates from 2 to the square root of the number and checks for divisors. If it finds any, it returns false. If it doesn't find any, it returns true.

In the end, the function isMultiplyPrime is tested with the input 30. It returns true, indicating that 30 is the product of three prime numbers (2, 3, and 5).

*/

/*
