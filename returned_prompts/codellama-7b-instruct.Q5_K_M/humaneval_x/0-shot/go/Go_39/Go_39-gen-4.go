	for {
		// Fibonacci sequence
		a, b := 0, 1
		for i := 0; i < n; i++ {
			a, b = b, a+b
		}

		// Check if it is prime
		if isPrime(a) {
			break A
		}
	}

	return a
}

func isPrime(n int) bool {
	// Check if number is divisible by 2 to n-1
	for i := 2; i < int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}
