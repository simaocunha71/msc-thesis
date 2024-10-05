func Factorize(n int) []int {
    factors := []int{}
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            factors = append(factors, i)
            for n%i == 0 {
                n /= i
            }
        }
    }
    if n != 1 {
        factors = append(factors, n)
    }
    return factors
}
