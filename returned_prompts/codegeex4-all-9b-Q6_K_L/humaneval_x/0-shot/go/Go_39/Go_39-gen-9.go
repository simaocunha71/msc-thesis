```go
func PrimeFib(n int) int {
    fib := [100]int{0, 1}
    for i := 2; i < len(fib); i++ {
        fib[i] = fib[i-1] + fib[i-2]
    }
    primes := [100]int{}
    isPrime := func(n int) bool {
        if n < 2 {
            return false
        }
        for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
            if n%i == 0 {
                return false
            }
        }
        return true
    }
    count := 0
    for i := 0; i < len(fib); i++ {
        if isPrime(fib[i]) {
            primes[count] = fib[i]
            count++
        }
    }
    return primes[n-1]
}
```

Explanation:

We start by defining a slice of integers `fib` with the first two Fibonacci numbers. Then we calculate the Fibonacci numbers up to the 100th number.

Next, we define a function `isPrime` that checks if a number is prime. This function iterates from 2 to the square root of the number and checks if the number is divisible by any of these values. If it is, the number is not prime.

Then we define an empty slice of integers `primes` to store the prime Fibonacci numbers. We iterate over the `fib` slice and check if each number is prime. If it is, we add it to the `primes` slice.

Finally, we return the n-th prime Fibonacci number by returning the n-th element of the `primes` slice.