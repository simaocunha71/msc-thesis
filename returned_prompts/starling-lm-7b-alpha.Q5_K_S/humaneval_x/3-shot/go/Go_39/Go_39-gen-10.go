    var current_fib = 0
    var prime_fib = 0
    var i = 3

    for current_fib < n {
        current_fib = fibonacci(i)
        if isPrime(current_fib) {
            prime_fib = current_fib
        }
        i += 1
    }
    return prime_fib
}

func fibonacci(n int) int {
    if n <= 1 {
        return n
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2)
    }
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    } else if n == 2 {
        return true
    } else if n%2 == 0 {
        return false
    } else {
        for i := 3; i*i <= n; i += 2 {
            if n % i == 0 {
                return false
            }
        }
        return true
    }
}



