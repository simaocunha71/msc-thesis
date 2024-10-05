    largest_factor := 1
    for i := 2; i * i <= n; i++ {
        for n % i == 0 {
            largest_factor = i
            n /= i
        }
    }
    return largest_factor
}