
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

	for n%3 == 0 {
		n /= 3
	}

	for i := 5; i*i <= n; i += 6 {
		if n%i == 0 {
			n /= i
		}
		for n%(i+2) == 0 {
			n /= i + 2
		}
	}
	if n > 1 {
		return n
	}
	return 0
}

// Return the number of prime factors of n.
// >>> PrimeFactors(13195)
// [5, 29, 11]
// >>> PrimeFactors(2048)
// [2, 2, 2, 2]
func PrimeFactors(n int) []int {

	var factors []int
	for n > 1 {
		p := LargestPrimeFactor(n)
		factors = append(factors, p)
		n /= p
	}
	return factors
}

// Return the number of prime factors of n.
// >>> PrimeFactors(13195)
// [5, 29, 11]
// >>> PrimeFactors(2048)
// [2, 2, 2, 2]
func PrimeFactors(n int) []int {

	var factors []int
	for n > 1 {
		p := LargestPrimeFactor(n)
		factors = append(factors, p)
		n /= p
	}
	return factors
}

// Return the