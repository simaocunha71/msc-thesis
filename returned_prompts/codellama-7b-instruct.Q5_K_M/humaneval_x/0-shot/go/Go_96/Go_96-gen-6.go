
	var res []int

	if n <= 0 {
		return res
	}

	for i := 2; i < n; i++ {
		if isPrime(i) {
			res = append(res, i)
		}
	}

	return res
}

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}

	for i := 2; i < n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

// https://stackoverflow.com/questions/40039692/how-to-implement-a-prime-generator
// https://play.golang.org/p/Uq_38MH54Q

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func CountUpTo(n int) []int {
	var res []int
	for i := 2; i <= n; i++ {
		if isPrime(i) {
			res = append(res, i)
		}
	}
	return res
}
