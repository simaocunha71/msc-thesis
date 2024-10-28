for _, word := range strings.Split(sentence, " ") {
	if len(word) > 1 && strings.Contains(word, " ") {
		continue
	}
	if isPrime(len(word)) {
		return word
	}
}

return ""
}

func isPrime(num int) bool {
	if num <= 1 {
		return false
	}
	for i := 2; i*i <= num; i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}

// 
func WordsInSentence(sentence string) string {
	
	for _, word := range strings.Split(sentence, " ") {
		if len(word) > 1 && strings.Contains(word, " ") {
			continue
		}
		if isPrime(len(word)) {
			return word
		}
	}
	
	return ""
}

func isPrime(num int) bool {
	if num <= 1 {
		return false
	}
	for i := 2; i*i <= num; i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}
