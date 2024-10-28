	for _, word := range strings.Fields(sentence) {
		if isPrime(len(word)) {
			return word
		}
	}
	return ""
}

func isPrime(num int) bool {
	if num == 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}
