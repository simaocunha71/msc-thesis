    var fibSeq []int
    var i int = 0
    for {
        fibNum := Fibonacci(i)
        if IsPrime(fibNum) {
            fibSeq = append(fibSeq, fibNum)
            if len(fibSeq) == n {
                return fibSeq[n-1]
            }
        }
        i++
    }
}

func Fibonacci(n int) int {
    if n <= 1 {
        return n
    }
    return Fibonacci(n-1) + Fibonacci(n-2)
}

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    if n == 2 {
        return true
    }
    if n%2 == 0 {
        return false
    }
    sqrtN := int(math.Sqrt(float64(n)))
    for i := 3; i <= sqrtN; i += 2 {
        if n%i == 0 {
            return false
        }
    }
    return true
}



