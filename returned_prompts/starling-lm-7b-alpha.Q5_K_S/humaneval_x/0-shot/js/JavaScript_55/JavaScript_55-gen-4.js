    if (n == 1) {
        return 1;
    } else if (n == 2) {
        return 2;
    } else {
        return fib(n - 1) + fib(n - 2);
    }
};

console.log(fib(10));
console.log(fib(1));
console.log(fib(8));

// console.log(fib(0));
// console.log(fib(3));
// console.log(fib(7));

*/

In this code, we define a function called fib that takes in a parameter n. The function calculates the n-th Fibonacci number using a recursive approach. 

The base cases are when n is equal to 1 or 2, in which case the function simply returns 1 or 2 respectively. 

For any other value of n, the function recursively calls itself with arguments n-1 and n-2, and adds the results together. This process continues until the base cases are reached. 

The function is then called with different values of n (10, 1, and 8) and the results are printed to the console. 

Note that the fibonacci sequence is defined as follows: fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2) for n > 1. However, in this code, we have not implemented the fib(0) case, as the Fibonacci sequence typically starts with fib(1) = 1. 

This code can be used to calculate Fibonacci numbers efficiently using recursion, but it may not be the most efficient approach for large values of n due to the repeated calculations involved in the recursion.

*/


































































































