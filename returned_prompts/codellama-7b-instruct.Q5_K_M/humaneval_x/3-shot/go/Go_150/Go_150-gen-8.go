    if is_prime(n) {
        return x
    }
    return y
}

func is_prime(n int) bool {
    for i := 2; i < n; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}



