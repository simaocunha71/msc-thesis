    var max_prime int
    for i := int(math.Sqrt(float64(n))); i > 1; i-- {
        if n%i == 0 {
            for ; n%i == 0; n /= i {
            }
            max_prime = i
        }
    }
    return max_prime
}