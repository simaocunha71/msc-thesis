
	hasLetter := false
	result := ""
	for _, c := range s {
		if unicode.IsLetter(c) {
			hasLetter = true
			if unicode.IsUpper(c) {
				result += strings.ToLower(string(c))
			} else {
				result += strings.ToUpper(string(c))
			}
		} else {
			result += string(c)
		}
	}

	if !hasLetter {
		return reverse(s)
	}

	return result
}

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// 