```go
func PrimeFib(n int) int {
    isPrime := func(x int) bool {
        if x < 2 {
            return false
        }
        for i := 2; i*i <= x; i++ {
            if x%i == 0 {
                return false
            }
        }
        return true
    }

    fib := func(n int) int {
        if n <= 1 {
            return n
        }
        a, b := 0, 1
        for i := 2; i <= n; i++ {
            a, b = b, a+b
        }
        return b
    }

    count := 0
    i := 2
    for {
        if isPrime(fib(i)) {
            count++
            if count == n {
                return fib(i)
            }
        }
        i++
    }
}
```
The above code defines a function `PrimeFib(n int) int` that returns the n-th Fibonacci number that is also prime. The function uses two helper functions: `isPrime` and `fib`.

The `isPrime` function checks if a given number `x` is prime. It returns `true` if `x` is prime, and `false` otherwise. The function iterates from 2 to the square root of `x` and checks if `x` is divisible by any number in this range. If `x` is divisible by any number in this range, it is not prime, and the function returns `false`. Otherwise, `x` is prime, and the function returns `true`.

The `fib` function calculates the n-th Fibonacci number. It uses an iterative approach to calculate the Fibonacci sequence. The function initializes two variables `a` and `b` to 0 and 1, respectively. It then iterates from 2 to `n` and updates `a` and `b` to `b` and `a+b`, respectively. After the iteration, `b` contains the n-th Fibonacci number, and the function returns `b`.

The `PrimeFib` function uses the `isPrime` and `fib` functions to find the n-th Fibonacci number that is also prime. It initializes a variable `count` to 0 and a variable `i` to 2. It then enters a loop that continues until it finds the n-th Fibonacci number that is prime. In each iteration of the loop, it checks if the i-th