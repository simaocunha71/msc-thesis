    max := -1
    for _, v := range lst {
        if v > max && isPrime(v) {
            max = v
        }
    }
    sum := 0
    if max != -1 {
        for _, c := range strconv.Itoa(max) {
            digit, _ := strconv.Atoi(string(c))
            sum += digit
        }
    }
    return sum
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i * i <= n; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}



