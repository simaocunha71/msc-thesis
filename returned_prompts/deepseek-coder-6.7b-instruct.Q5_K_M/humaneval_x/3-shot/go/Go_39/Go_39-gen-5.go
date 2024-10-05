    fib_seq := make([]int, 0)
    fib_seq = append(fib_seq, 2)

    i := 3
    for {
        if isPrime(i) && isFib(i, fib_seq) {
            fib_seq = append(fib_seq, i)
        }
        if len(fib_seq) == n {
            break
        }
        i++
    }
    return fib_seq[n-1]
}

func isPrime(n int) bool {
    if n == 2 {
        return true
    }
    if n % 2 == 0 || n == 1 {
        return false
    }

    sqrtN := int(math.Sqrt(float64(n)))
    for i := 3; i <= sqrtN; i += 2 {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func isFib(n int, fib_seq []int) bool {
    a, b := 0, 1
    for b <= n {
        a, b = b, a+b
        if b == n {
            return true
        }
    }
    return false
}



