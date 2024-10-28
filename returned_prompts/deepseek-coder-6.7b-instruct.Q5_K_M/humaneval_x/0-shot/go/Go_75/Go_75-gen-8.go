
	primeCheck := func(n int) bool {
		if n == 1 {
			return false
		}
		if n == 2 {
			return true
		}
		for i := 2; i*i <= n; i++ {
			if n%i == 0 {
				return false
			}
		}
		return true
	}

	count := 0
	for i := 2; i <= a; i++ {
		if a%i == 0 && primeCheck(i) {
			count++
		}
	}

	if count >= 3 {
		return true
	} else {
		return false
	}
}

