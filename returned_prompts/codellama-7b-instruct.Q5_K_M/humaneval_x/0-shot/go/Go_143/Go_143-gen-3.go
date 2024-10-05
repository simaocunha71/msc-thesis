	for i, v := range sentence {
		if v == ' ' {
			sentence = sentence[i+1:]
			goto A
		}
	}

	var words []string
	for _, word := range strings.Split(sentence, " ") {
		if isPrime(len(word)) {
			words = append(words, word)
		}
	}

	return strings.Join(words, " ")
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
