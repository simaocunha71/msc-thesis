    largest_prime := 0
    for _, num := range lst {
        if IsPrime(num) && num > largest_prime {
            largest_prime = num
        }
    }
    digit_sum := 0
    for _, digit := range strconv.Itoa(largest_prime) {
        digit_sum += int(digit - '0')
    }
    return digit_sum
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


