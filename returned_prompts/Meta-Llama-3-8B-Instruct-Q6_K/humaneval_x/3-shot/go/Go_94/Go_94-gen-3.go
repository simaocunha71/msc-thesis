    max_prime := 0
    for _, num := range lst {
        if num > max_prime && IsPrime(num) {
            max_prime = num
        }
    }
    return SumOfDigits(max_prime)
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

func SumOfDigits(n int) int {
    sum := 0
    for n > 0 {
        sum += int(n % 10)
        n /= 10
    }
    return sum
}