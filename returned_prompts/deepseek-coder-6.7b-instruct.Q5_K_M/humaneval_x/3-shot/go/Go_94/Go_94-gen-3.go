    max_prime := 0
    for i := 0; i < len(lst); i++ {
        if is_prime(lst[i]) && lst[i] > max_prime {
            max_prime = lst[i]
        }
    }
    return sum_of_digits(max_prime)
}

func is_prime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func sum_of_digits(n int) int {
    sum := 0
    for n > 0 {
        sum += n % 10
        n /= 10
    }
    return sum
}



