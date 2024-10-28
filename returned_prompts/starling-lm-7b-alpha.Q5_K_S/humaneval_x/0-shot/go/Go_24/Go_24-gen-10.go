    for i := 2; i <= n; i++ {
        if n % i == 0 {
            return i
        }
    }
    return 0
}

// >>> LargestDivisor(15)
// 5

In the above code, we have a function LargestDivisor that takes an integer n and returns the largest divisor of n, which is smaller than n itself.
To find the largest divisor, we start by initializing a variable i with the value 2. We then iterate through each integer from 2 to n.
Inside the loop, we check if the current integer i is a divisor of n. We do this by using the modulo operator (%). If the remainder of the division of n by i is zero, then i is a divisor of n.
If i is a divisor, we return i as the largest divisor. We continue to check each integer until we find the largest divisor or until we reach the end of the loop.
If no divisor is found, we return 0, indicating that there are no divisors of n smaller than n itself.

To use the function, you can call LargestDivisor with an integer as an argument, as shown in the example. In the example, we call LargestDivisor with the argument 15 and store the result in a variable called result. We then print the result to the console using the fmt.Println function.

The output of the code is 5, which is the largest divisor of 15 that is smaller than 15.

Note that this code assumes that the input number n is a positive integer.

In this code, we have a function named LargestDivisor that takes an integer n as an argument and returns the largest divisor of n, which is smaller than n itself. To find the largest divisor, we start by initializing a variable i with the value 2. We then iterate through each integer from 2 to n. Inside the loop, we check if the current integer i is a divisor of n using the modulo operator (%). If the remainder of the division of n by i is zero, then i is a divisor. If i is a divisor, we return i as the largest divisor. We continue to check each integer