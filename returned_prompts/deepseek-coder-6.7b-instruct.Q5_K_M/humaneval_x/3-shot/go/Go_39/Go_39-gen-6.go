    // function to check if the number is prime
    isPrime := func(num int) bool {
        if num < 2 {
            return false
        }
        for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
            if num%i == 0 {
                return false
            }
        }
        return true
    }

    // function to generate Fibonacci numbers
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

    // generate Fibonacci numbers and check if they are prime
    count := 0
    i := 0
    for count < n {
        i++
        if isPrime(fib(i)) {
            count++
        }
    }
    return fib(i)
}



