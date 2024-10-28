	i := 1
	j := 1
	count := 0
	for {
		temp := i
		i += j
		j = temp
		if isPrime(i) {
			count++
			if count == n {
				return i
			}
		}
	}
	return 0
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
	sqrt := int(math.Sqrt(float6y(n)))
	for i := 3; i <= sqrt; i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

