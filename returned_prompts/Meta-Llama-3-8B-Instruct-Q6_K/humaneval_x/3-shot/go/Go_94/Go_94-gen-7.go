    max_prime := 0
    for _, n := range lst {
        if isPrime(n) && n > max_prime {
            max_prime = n
        }
    }
    sum := 0
    for _, d := range strconv.FormatInt(int64(max_prime), 10) {
        sum += int(d - '0')
    }
    return sum
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}