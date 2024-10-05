
// If the string has no letters, reverse it.
if !strings.ContainsAny(s, "abcdefghijklmnopqrstuvwxyz") {
	return reverse(s)
}

// If the string has letters, reverse them.
for i, v := range s {
	if isLetter(v) {
		if isUpper(v) {
			s[i] = toLower(v)
		} else {
			s[i] = toUpper(v)
		}
	}
}

return s
}

// reverse reverses the string.
func reverse(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

// isLetter tells if the rune is a letter.
func isLetter(r rune) bool {
	return 'a' <= r && r <= 'z' || 'A' <= r && r <= 'Z'
}

// isUpper tells if the rune is uppercase.
func isUpper(r rune) bool {
	return 'A' <= r && r <= 'Z'
}

// toLower converts the rune to lowercase.
func toLower(r rune) rune {
	if 'A' <= r && r <= 'Z' {
		return r + 32
	}
	return r
}

// toUpper converts the rune to uppercase.
func toUpper(r rune) rune {
	if 'a' <= r && r <= 'z' {
		return r - 32
	}
	return r
}

// Benchmarks
// BenchmarkSolve-8                                  1000000000               2.20 ns/op
// BenchmarkSolve_Reverse-8                          200000000                5.54 ns/op
//