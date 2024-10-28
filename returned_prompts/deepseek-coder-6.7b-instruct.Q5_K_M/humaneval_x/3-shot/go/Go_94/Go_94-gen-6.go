    is_prime := func (n int) bool {
        if n < 2 {
            return false
        }
        for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
            if n % i == 0 {
                return false
            }
        }
        return true
    }

    max_prime := -1
    for _, v := range lst {
        if is_prime(v) && v > max_prime {
            max_prime = v
        }
    }
    if max_prime == -1 {
        return -1
    }
    digit_sum := 0
    for max_prime > 0 {
        digit_sum += max_prime % 10
        max_prime /= 10
    }
    return digit_sum
}



