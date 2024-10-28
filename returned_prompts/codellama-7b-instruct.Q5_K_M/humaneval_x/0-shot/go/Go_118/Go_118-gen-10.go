	for i := 0; i < len(word); i++ {
		if !isVowel(word[i]) {
			for j := i + 1; j < len(word); j++ {
				if isVowel(word[j]) {
					return string(word[j])
				}
			}
		}
	}
	return ""
}

func isVowel(c byte) bool {
	switch c {
	case 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U':
		return true
	}
	return false
}
