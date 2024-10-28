```go
func PrimeFib(n int) int {
    a, b := 1, 1
    count := 0
    for {
        a, b = b, a+b
        if isPrime(b) {
            count++
            if count == n {
                return b
            }
        }
    }
}

func isPrime(num int) bool {
    if num <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
        if num%i == 0 {
            return false
        }
    }
    return true
}
```


Explanation:
The `PrimeFib` function generates Fibonacci numbers and checks if they are prime using the `isPrime` function. The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of the iterated values. If the number is not divisible, it is prime. The `PrimeFib` function returns the nth Fibonacci number that is also prime. The function uses a loop to generate Fibonacci numbers and checks if each number is prime using the `isPrime` function. When the nth prime Fibonacci number is found, the function returns it.