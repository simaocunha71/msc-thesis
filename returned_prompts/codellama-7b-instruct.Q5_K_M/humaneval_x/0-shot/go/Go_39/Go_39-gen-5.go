	for i := math.MaxInt64; i > 0; i-- {
		if isFibPrime(i) {
			if n == 1 {
				return int(i)
			}
			n--
		}
	}
	panic("not found")
}

func isFibPrime(n int64) bool {
	a, b := 0, 1
	for b < n {
		a, b = b, a+b
	}
	return isPrime(a)
}

func isPrime(n int64) bool {
	if n <= 1 {
		return false
	}
	for i := int64(2); i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}
