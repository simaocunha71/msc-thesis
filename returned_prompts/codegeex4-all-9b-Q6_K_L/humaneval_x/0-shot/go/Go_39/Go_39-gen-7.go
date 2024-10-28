func PrimeFib(n int) int {
	if n < 1 {
		return -1
	}
	var a, b, c int = 1, 1, 2
	for i := 3; i <= n; i++ {
		a = b
		b = c
		c = a + b
		if isPrime(c) {
			return c
		}
	}
	return -1
}

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	sqrt := int(math.Sqrt(float64(n)))
	for i := 3; i <= sqrt; i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}
