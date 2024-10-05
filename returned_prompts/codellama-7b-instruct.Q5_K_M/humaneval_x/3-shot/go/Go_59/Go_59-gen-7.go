    for i := n; i > 1; i-- {
        if n % i == 0 {
            if isPrime(i) {
                return i
            }
        }
    }
    return 1
}

func isPrime(n int) bool {
    if n == 1 {
        return false
    }

    for i := 2; i < n; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}



