    var primeFib int = 0
    var count int = 0
    var fib1 int = 0
    var fib2 int = 1
    for count < n {
        if isPrime(fib1) {
            primeFib++
        }

        if primeFib == n {
            break
        }

        temp := fib1
        fib1 = fib2
        fib2 = temp + fib1
        count++
    }
    return fib1

}

func isPrime(n int) bool {
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

