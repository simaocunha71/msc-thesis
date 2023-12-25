
// Return the largest prime factor of n. Assume n > 1 and is not a prime.
// >>> LargestPrimeFactor(13195)
// 29
// >>> LargestPrimeFactor(2048)
// 2
func LargestPrimeFactor(n int) int {
    var s = n
    for i := 2; i*i <= n; i++ {
        if (s/i)%i != 0 && !(s/(i*(i-1)))%i == 0 {
            break
        }
    }
    return s / (i * (i - 1)) // get largest prime factor to n
}
