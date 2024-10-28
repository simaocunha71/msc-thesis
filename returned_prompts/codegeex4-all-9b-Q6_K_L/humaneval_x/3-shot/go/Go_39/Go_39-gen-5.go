    fib := func(n int) int {
        if n <= 1 {
            return n
        }
        return fib(n-1) + fib(n-2)
    }

    isPrime := func(num int) bool {
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

    count := 0
    for i := 2; ; i++ {
        if isPrime(fib(i)) {
            count++
            if count == n {
                return fib(i)
            }
        }
    }
}

