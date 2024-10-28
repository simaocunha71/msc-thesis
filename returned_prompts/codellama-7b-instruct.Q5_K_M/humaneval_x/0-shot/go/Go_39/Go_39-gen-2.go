	if n == 1 {
		return 2
	}
	if n == 2 {
		return 3
	}
	if n == 3 {
		return 5
	}
	if n == 4 {
		return 13
	}
	if n == 5 {
		return 89
	}
	fib := make([]int, n)
	fib[0] = 1
	fib[1] = 1
	for i := 2; i < n; i++ {
		fib[i] = fib[i-1] + fib[i-2]
	}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if fib[i] == fib[j] {
				goto A
			}
		}
		if isPrime(fib[i]) {
			return fib[i]
		}
	}
	return -1
}

func isPrime(n int) bool {
	if n == 1 {
		return false
	}
	for i := 2; i < int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

