    fib := func(n int) int {
        if n <= 1 {
            return n
        }
        return fib(n-1) + fib(n-2)
    }

    isPrime := func(n int) bool {
        if n <= 1 {
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
    for i := 0; count < n; i++ {
        if isPrime(fib(i)) {
            count++
        }
    }
    return fib(count)
}

B:
    fib := func(n int) int {
        if n <= 1 {
            return n
        }
        return fib(n-1) + fib(n-2)
    }

    isPrime := func(n int) bool {
        if n <= 1 {
            return false
        }
        for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
            if n%i == 0 {
                return false
            }
        }
        return true
    }

    for i := 0; ; i++ {
        if isPrime(fib(i)) {
            if i == n {
                return fib(i)
            }
        }
    }
}

C:
    fib := func(n int) int {
        if n <= 1 {
            return n
        }
        return fib(n-1) + fib(n-2)
    }

    isPrime := func(n int) bool {
        if n <= 1 {
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
    for i := 0; count < n; i++ {
        if isPrime(fib(i)) {
            count++
        }
    }
    return fib(i - 1)
}

D:
    fib := func(n int) int {
        if n <= 1 {
            return n
        }
        return fib(n-1) + fib(n-2)
    }

    isPrime := func(n int) bool {
        if n <= 1 {
            return false
        }
        for i := 2; i <= int(math.Sqrt(float64(n))); i++