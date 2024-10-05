	if n <= 0 {
		return 0
	}
	if n == 1 {
		return 2
	}
	if n == 2 {
		return 3
	}
	c := 3
	f := 5
	for i := 3; i < n; i++ {
		c, f = fibo(f, c+f)
		if isPrime(f) {
			return f
		}
	}
	return 0
}

func fibo(a, b int) (int, int) {
	return b, a+b
}

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n <= 3 {
		return true
	}
	if n%2 == 0 || n%3 == 0 {
		return false
	}
	r := int(math.Sqrt(float64(n)))
	f := 5
	for f <= r {
		if n%f == 0 || n%(f+2) == 0 {
			return false
		}
		f += 6
	}
	return true
}




















































































































































































































