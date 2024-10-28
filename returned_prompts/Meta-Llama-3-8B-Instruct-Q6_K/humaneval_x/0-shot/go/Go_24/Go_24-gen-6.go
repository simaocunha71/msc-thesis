The largest divisor of n smaller than n is the largest prime factor of n. You can use a function to find the prime factors of n and then return the largest one.

Here is the code:

```go
func LargestDivisor(n int) int {
    var maxDivisor int
    for i := n / 2; i > 1; i-- {
        if n%i == 0 {
            maxDivisor = i
            break
        }
    }
    return maxDivisor
}
```

This function works by looping down from n/2 to 1 and checking if each number is a divisor of n. The first one it finds that is a divisor is the largest divisor smaller than n.

However, this function is not efficient for large numbers, because it checks every number down to 1. A more efficient function would be one that only checks prime numbers, because a composite number must have a prime factor less than or equal to its square root. Here is such a function:

```go
func LargestDivisor(n int) int {
    for i := int(math.Sqrt(float64(n))); i > 1; i-- {
        if n%i == 0 {
            return i
        }
        for j := 2; j*j <= i; j++ {
            if i%j == 0 {
                break
            }
        } else {
            return i
        }
    }
    return 1
}
```

This function works by looping down from the square root of n to 1, and checking if each number is a divisor of n. If it is, it returns that number. If it finds a number that is not a divisor, it returns the previous number that was a divisor. If no divisors are found, it returns 1.

This function is much more efficient for large numbers, because it only checks a fraction of the numbers that the previous function checked. However, it is still not the most efficient function possible, because it checks every prime number down to the square root of n. A more efficient function would be one that only checks the prime numbers that are less than or equal to the square root of n, and that stops checking as soon as it finds a divisor. Here is such a function:

```go
func LargestDivisor(n int) int {
    for i := int(math.Sqrt(float64(n))); i > 1; i-- {
        if n%i == 0 {
            return i
        }
        if Is