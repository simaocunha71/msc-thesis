    if n == 1{
        return 2
    }

    if n == 2{
        return 3
    }

    for i := 3; i < math.MaxInt32; i += 2 {
        if IsFibonacciPrime(i) && IsFibonacciPrime(i+1) {
            if n == 3 {
                return i
            }
            n -= 2
        }
    }
    return -1
}

// Check if a number is a prime number.
func IsPrime(number int) bool {
    if number == 1 {
        return false
    }
    for i := 2; i < math.Sqrt(float64(number)); i++ {
        if number%i == 0 {
            return false
        }
    }
    return true
}

// Check if a number is a prime Fibonacci number.
func IsFibonacciPrime(number int) bool {
    if !IsPrime(number) {
        return false
    }
    for i := 0; i < 50; i++ {
        if number != Fibonacci(i) && IsPrime(Fibonacci(i)) {
            return false
        }
    }
    return true
}

// Calculate n-th Fibonacci number
func Fibonacci(n int) int {
    if n == 0 {
        return 0
    }
    if n == 1 {
        return 1
    }
    return Fibonacci(n-1) + Fibonacci(n-2)
}



