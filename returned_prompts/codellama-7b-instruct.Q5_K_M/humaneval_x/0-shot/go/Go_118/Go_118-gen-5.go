	for i := range word {
		if i == 0 {
			continue
		}
		if !isVowel(word[i]) {
			if isVowel(word[i-1]) {
				return string(word[i-1])
			}
			continue
		}
		if i == len(word)-1 {
			if isVowel(word[i]) {
				return string(word[i])
			}
			continue
		}
		if isVowel(word[i+1]) {
			return string(word[i+1])
		}
	}
	return ""
}

func isVowel(b byte) bool {
	switch b {
	case 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U':
		return true
	}
	return false
}
