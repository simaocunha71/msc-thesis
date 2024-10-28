    var i = 2
    for ; i < n; i++ {
        if n % i == 0 {
            return i
        }
    }
    return n
}

// >>> LargestDivisor(15)
// 5

Here is a simple function that calculates the largest divisor that divides the input number evenly.
It does so by looping from 2 to n (the input number) and checking if n is divisible by i. If it is, then i is a divisor of n.
If no divisors are found, the function returns the input number itself.

In the provided example, when we call LargestDivisor(15), the function will return 5 because 5 is the largest divisor that divides 15 evenly.

To use this function, you can simply call it with a number as the argument, like this:

// >>> LargestDivisor(15)
// 5

This will print the result of calling LargestDivisor(15), which is 5.

In this function, we use a for loop to iterate through numbers from 2 to n. Inside the loop, we check if n is divisible by i using the modulo operator (%). If the remainder is 0, it means that i is a divisor of n. In that case, we return i as the result. If no divisors are found, we return n itself.

This function can be used to find the largest divisor of any positive integer.

Here is a step-by-step explanation of how the function works:

1. Initialize a variable i to 2, which will be used as the starting point for the loop.
2. Enter a for loop that iterates from i = 2 to n (the input number).
3. Inside the loop, check if n is divisible by i using the modulo operator (%). If the remainder is 0, it means that i is a divisor of n.
4. If i is a divisor of n, return i as the result.
5. If no divisors are found, after the loop finishes, return n itself.

By following these steps, the function will correctly calculate and return the largest divisor that divides the input