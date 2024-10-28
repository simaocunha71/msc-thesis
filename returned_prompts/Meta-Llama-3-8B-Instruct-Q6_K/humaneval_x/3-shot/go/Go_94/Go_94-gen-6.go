    var max_prime int
    max_prime_sum int
    for _, num := range lst {
        if isPrime(num) {
            if num > max_prime {
                max_prime = num
                max_prime_sum = sumOfDigits(max_prime)
            }
        }
    }
    return max_prime_sum

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

func sumOfDigits(n int) int {
    sum := 0
    for _, d := range strconv.Itoa(n) {
        sum += int(d - '0')
    }
    return sum
}