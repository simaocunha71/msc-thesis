    primeFib := make([]int, 0)
    fib1, fib2, fibTemp := 0, 1, 0
    for i := 2; ; i++ {
        fibTemp = fib1 + fib2
        fib1 = fib2
        fib2 = fibTemp
        if IsPrime(fibTemp) {
            primeFib = append(primeFib, fibTemp)
        }
        if len(primeFib) == n {
            return primeFib[n-1]
        }
    }
}

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    sqrtN := int(math.Sqrt(float64(n)))
    for i := 2; i <= sqrtN; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}



