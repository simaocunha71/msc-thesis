    i := n - 1
    for i > 1 {
        if isPrime(i) {
            return i
        }
        i--
    }
    return 1
}

func isPrime(num int) bool {
    if num <= 1 {
        return false
    }
    for i := 2; i * i <= num; i++ {
        if num%i == 0 {
            return false
        }
    }
    return true
}