	if n < 1 {
		panic("n should be greater than 0")
	}

	var (
		a, b int
	)

	for a = 0; a < n; a++ {
		b = int(math.Floor(math.Sqrt(5*math.Pow(float64(a), 2) + 0.25) - 0.5))
		if isPrime(b) {
			continue A
		}
	}

	return b
}

func isPrime(n int) bool {
	if n < 2 {
		return false
	}

	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}

	return true
}
