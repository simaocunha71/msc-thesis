
}

*/

// LargestPrimeFactor returns the largest prime factor of n.
func LargestPrimeFactor(n int) int {

	// Start with the smallest prime number 2.
	i := 2

	// While n is divisible by i...
	for n%i == 0 {

		// Divide n by i and set n equal to the result.
		n = n / i

	}

	// Increment i by 1.
	i++

	// While i is less than or equal to the square root of n...
	for i*i <= n {

		// While n is divisible by i...
		for n%i == 0 {

			// Divide n by i and set n equal to the result.
			n = n / i

		}

		// Increment i by 2.
		i += 2

	}

	// Return n, which at this point should be the largest prime factor.
	return n

}

// LargestPrimeFactorV2 returns the largest prime factor of n.
func LargestPrimeFactorV2(n int) int {

	// Start with the largest prime number possible.
	i := n

	// While i is greater than 1...
	for i != 1 {

		// If n is divisible by i and i is a prime number...
		if n%i == 0 && IsPrime(i) {

			// Return i.
			return i

		}

		// Decrement i by 1.
		i--

	}

	// Return 1 if no prime factors are found.
	return 1

}

// IsPrime checks if a number is a prime number.
func IsPrime(n int) bool {

	// If n is less than 2, it is not a prime number.
	if n < 2 {

		return false

	}

	// If n is 2, it is a prime number.
	if n == 2 {

		return true

	}

	// If n is divisible by any number up to the square root of n, it is not a prime number.
	for i