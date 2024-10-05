    var largest_prime_factor int
    for i := 2; i <= n; i++ {
        if n%i == 0 {
            for j := i; j <= n/i; j++ {
                if n % j == 0 {
                    break
                }
            } else {
                largest_prime_factor = i
            }
        }
    }
    return largest_prime_factor
}