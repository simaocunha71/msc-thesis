
	if interval1[1] < interval2[0] || interval1[0] > interval2[1] {
		return "NO"
	}

	if interval1[0] < interval2[0] {
		interval1[0] = interval2[0]
	}

	if interval1[1] > interval2[1] {
		interval1[1] = interval2[1]
	}

	if interval1[1]-interval1[0] > 1 {
		return "NO"
	}

	if IsPrime(interval1[1]-interval1[0]) {
		return "YES"
	}

	return "NO"
}

func IsPrime(n int) bool {
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
