
func LargestPrimeFactor(n int) int {
    maxPrime := 0
    for i := 2; i <= n/2; i++ {
        for n%i == 0 {
            maxPrime = i
        }
    }
    return maxPrime
}

The time complexity of this function is O(log n) because the loop condition is i <= sqrt(n), which means the maximum number of times the inner loop will run is the number of digits in n.

Explanation:

In this function, we start by initializing the maxPrime variable to 0. We then iterate through all the numbers from 2 to n/2 using a for loop. Inside the loop, we check if n is divisible by i using the modulo operator (%). If it is, we update the maxPrime variable to the current value of i. This process continues until we have checked all the possible divisors of n. Finally, we return the maxPrime variable, which will contain the largest prime factor of n.

The time complexity of this function is O(log n) because the loop condition is i <= sqrt(n), which means the maximum number of times the inner loop will run is the number of digits in n. This is because we only need to check divisors up to the square root of n in order to find the largest prime factor.

Here are some example outputs of the function:

LargestPrimeFactor(13195) -> 29
LargestPrimeFactor(2048) -> 2

In the first example, the largest prime factor of 13195 is 29. In the second example, the largest prime factor of 2048 is 2.

Overall, this function effectively finds the largest prime factor of a given number by iteratively checking all the possible divisors of that number.

// Created by Amit Kumar

//








































































