func LargestPrimeFactor(n int) int {
    primeFactors := make([]int, 0)
    for i := 2; i <= n; i++ {
        for n%i == 0 {
            primeFactors = append(primeFactors, i)
            n = n / i
        }
    }
    return primeFactors[len(primeFactors)-1]
}