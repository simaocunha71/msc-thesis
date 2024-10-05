    fib := make([]int, 0)
    fib = append(fib, 0, 1)

    for {
        next := fib[len(fib)-1] + fib[len(fib)-2]
        fib = append(fib, next)

        if isPrime(next) {
            n -= 1
        }

        if n == 0 {
            return next
        }
    }
}

func isPrime(n int) bool {
    if n == 1 || (n%2 == 0 && n > 2) {
        return false
    }

    for i := 3; i*i <= n; i += 2 {
        if n%i == 0 {
            return false
        }
    }

    return true
}

