    var max_prime int = 0
    for _, number := range lst {
        if number > max_prime && IsPrime(number) {
            max_prime = number
        }
    }
    return SumDigits(max_prime)
}

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i < int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func SumDigits(n int) int {
    sum := 0
    for n != 0 {
        sum += n % 10
        n /= 10
    }
    return sum
}

