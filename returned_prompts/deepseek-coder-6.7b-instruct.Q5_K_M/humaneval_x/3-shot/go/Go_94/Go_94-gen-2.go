    max_prime := 0
    for _, num := range lst {
        if is_prime(num) && num > max_prime {
            max_prime = num
        }
    }

    return sum_of_digits(max_prime)
}

func is_prime(n int) bool {
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

func sum_of_digits(n int) int {
    sum := 0
    for n > 0 {
        digit := n % 10
        sum += digit
        n /= 10
    }
    return sum
}



