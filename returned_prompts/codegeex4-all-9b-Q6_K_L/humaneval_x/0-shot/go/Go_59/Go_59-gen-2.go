Here is a solution using Go:

```go
func LargestPrimeFactor(n int) int {
    // The largest prime factor of a number is always less than or equal to the square root of that number.
    // So, we only need to check for prime factors up to the square root of n.
    maxPrime := int(math.Sqrt(float64(n)))
    for i := 2; i <= maxPrime; i++ {
        // If n is divisible by i, then i is a factor of n.
        // If n is divisible by i, then we divide n by i and check for more factors.
        for n%i == 0 {
            n = n / i
        }
    }
    // If n is a prime number, then it will be greater than 1 and less than or equal to the square root of the original n.
    // So, n is the largest prime factor of the original n.
    return n
}
```
This function works by iterating over all numbers from 2 to the square root of n. If n is divisible by the current number, it divides n by that number and checks for more factors. If n is a prime number, it will be greater than 1 and less than or equal to the square root of the original n. So, if the loop finishes, n is the largest prime factor of the original n.