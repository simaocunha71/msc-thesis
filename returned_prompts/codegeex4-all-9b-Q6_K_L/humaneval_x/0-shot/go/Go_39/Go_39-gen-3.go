func PrimeFib(n int) int {
	if n == 1 {
		return 2
	}

	if n == 2 {
		return 3
	}

	a, b := 2, 3
	for i := 3; i <= n; i++ {
		c := a + b
		if isPrime(c) {
			a, b = b, c
		} else {
			a, b = b, c
			i--
		}
	}
	return b
}

func isPrime(n int) bool {
	if n < 2 {
		return false
	}

	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}

	return true
}

