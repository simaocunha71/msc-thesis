    factors := make([]int, 0)
    for i := 2; i * i <= n; i++ {
        count := 0
        for n % i == 0 {
            n /= i
            count++
        }
        if count > 0 {
            factors = append(factors, int32(i))
            for count > 0 {
                factors = append(factors, int32(i))
                count--
            }
        }
    }
    if n > 1 {
        factors = append(factors, int32(n))
    }
    return factors
}