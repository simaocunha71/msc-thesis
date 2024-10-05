
// Return the largest prime factor of n. Assume n > 1 and is not a prime.
// >>> LargestPrimeFactor(13195)
// 29
// >>> LargestPrimeFactor(2048)
// 2
func LargestPrimeFactor(n int) int {
	// 1. Initialize largest prime factor to 1.
	largestPrimeFactor := 1
	// 2. Initialize largest prime factor to 2.
	largestPrimeFactor = 2
	// 3. Loop from 3 to n, incrementing by 2.
	for i := 3; i <= n; i += 2 {
		// 4. If i divides n, then i is a factor and largestPrimeFactor should be set to i.
		if n%i == 0 {
			largestPrimeFactor = i
			// 5. Break out of the loop, since we have found the largest prime factor.
			break
		}
	}
	return largestPrimeFactor
}
