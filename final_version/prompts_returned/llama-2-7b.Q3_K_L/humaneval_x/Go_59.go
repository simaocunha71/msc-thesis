
// Return the largest prime factor of n. Assume n > 1 and is not a prime.
// >>> LargestPrimeFactor(13195)
// 29
// >>> LargestPrimeFactor(2048)
// 2
func LargestPrimeFactor(n int) int {
    var d = n
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            if d > (n / i) {
                return i
            } else {
                d = (n / i)
            }
        }
    }
    return d
}