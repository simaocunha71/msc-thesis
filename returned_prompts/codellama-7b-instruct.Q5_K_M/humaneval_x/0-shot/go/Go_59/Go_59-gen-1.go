
// Return the largest prime factor of n. Assume n > 1 and is not a prime.
// >>> LargestPrimeFactor(13195)
// 29
// >>> LargestPrimeFactor(2048)
// 2
func LargestPrimeFactor(n int) int {

	// 1. If n is a prime, return n.
	if IsPrime(n) {
		return n
	}

	// 2. If n has no prime factors, return n.
	if !HasPrimeFactors(n) {
		return n
	}

	// 3. If n is divisible by 2, return the largest prime factor of n/2.
	if n%2 == 0 {
		return LargestPrimeFactor(n / 2)
	}

	// 4. If n is divisible by 3, return the largest prime factor of n/3.
	if n%3 == 0 {
		return LargestPrimeFactor(n / 3)
	}

	// 5. If n is divisible by 5, return the largest prime factor of n/5.
	if n%5 == 0 {
		return LargestPrimeFactor(n / 5)
	}

	// 6. If n is divisible by 7, return the largest prime factor of n/7.
	if n%7 == 0 {
		return LargestPrimeFactor(n / 7)
	}

	// 7. If n is divisible by 11, return the largest prime factor of n/11.
	if n%11 == 0 {
		return LargestPrimeFactor(n / 11)
	}

	// 8. If n is divisible by 13, return the largest prime factor of n/13.
	if n%13 == 0 {
		return LargestPrimeFactor(n / 13)
	}

	// 9. If n is divisible by 17, return