
// Return the largest prime factor of n. Assume n > 1 and is not a prime.
// >>> LargestPrimeFactor(13195)
// 29
// >>> LargestPrimeFactor(2048)
// 2
func LargestPrimeFactor(n int) int {

	if n%2 == 0 {
		for n%2 == 0 {
			n /= 2
		}
	}
	for i := 3; i*i <= n; i += 2 {
		for n%i == 0 {
			n /= i
		}
	}
	return n
}

