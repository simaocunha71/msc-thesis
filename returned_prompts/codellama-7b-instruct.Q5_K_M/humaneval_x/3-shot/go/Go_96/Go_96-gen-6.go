    var prime_numbers := make([]int, 0)
    for i := 2; i < n; i++ {
        var is_prime := true
        for j := 2; j < int(math.Sqrt(float64(i))); j++ {
            if i%j == 0 {
                is_prime = false
                break
            }
        }
        if is_prime {
            prime_numbers = append(prime_numbers, i)
        }
    }
    return prime_numbers
}



