    max := math.MinInt
    for _, n := range lst {
        if isPrime(n) && n > max {
            max = n
        }
    }
    if max == math.MinInt {
        return 0
    }
    sum := 0
    for _, d := range strconv.Itoa(max) {
        digit, _ := strconv.Atoi(string(d))
        sum += digit
    }
    return sum
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

