    max_prime := 0
    for _, num := range lst {
        if isPrime(num) {
            max_prime = num
        }
    }
    return sumDigits(max_prime)
}

func isPrime(num int) bool {
    for i := 2; i*i <= num; i++ {
        if num % i == 0 {
            return false
        }
    }
    return true
}

func sumDigits(num int) int {
    sum := 0
    for num > 0 {
        sum += num % 10
        num /= 10
    }
    return sum
}




