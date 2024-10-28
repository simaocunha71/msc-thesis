
	// check if the string contains any letter
	// if not, reverse the string
	for _, r := range s {
		if unicode.IsLetter(r) {
			goto B
		}
	}
	return reverse(s)

B:
	// otherwise reverse the letters
	b := make([]rune, len(s))
	for i, r := range s {
		if unicode.IsLetter(r) {
			if unicode.IsLower(r) {
				r = unicode.ToUpper(r)
			} else {
				r = unicode.ToLower(r)
			}
		}
		b[len(s)-i-1] = r
	}
	return string(b)
}
