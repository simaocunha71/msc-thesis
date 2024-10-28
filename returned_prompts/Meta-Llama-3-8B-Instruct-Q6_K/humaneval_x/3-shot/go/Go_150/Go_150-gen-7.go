    if isPrime(n) {
        return x
    } else {
        return y
    }
}

// helper function to check if a number is prime
func isPrime(num int) bool {
    if num <= 1 {
        return false
    }
    for i := 2; i*i <= num; i++ {
        if num%i == 0 {
            return false
        }
    }
    return true
}