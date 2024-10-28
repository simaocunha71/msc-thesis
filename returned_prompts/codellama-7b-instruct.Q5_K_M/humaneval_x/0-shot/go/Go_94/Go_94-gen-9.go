    for _, v := range lst {
        if isPrime(v) {
            return sumDigits(v)
        }
    }
    return 0
}

func sumDigits(n int) int {
    s := strconv.Itoa(n)
    sum := 0
    for _, v := range s {
        sum += int(v - '0')
    }
    return sum
}

func isPrime(n int) bool {
    if n < 2 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}
