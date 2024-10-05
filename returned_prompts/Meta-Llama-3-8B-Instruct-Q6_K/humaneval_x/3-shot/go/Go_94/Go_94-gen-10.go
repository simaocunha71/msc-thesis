    max_prime := 0
    for _, v := range lst {
        if IsPrime(v) && v > max_prime {
            max_prime = v
        }
    }
    return sumOfDigits(max_prime)
}

func IsPrime(n int) bool {
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

func sumOfDigits(n int) int {
    sum := 0
    for n > 0 {
        sum += int(n % 10)
        n /= 10
    }
    return sum
}