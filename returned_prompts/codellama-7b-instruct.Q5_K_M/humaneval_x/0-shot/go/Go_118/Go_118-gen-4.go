	for i := len(word) - 1; i >= 0; i-- {
		if isVowel(word[i]) {
			return word[i : i+1]
		}
		if isConsonant(word[i]) {
			continue
		}
		return ""
	}
	return ""
}

func isConsonant(r rune) bool {
	return r == 'c' || r == 'k' || r == 'g' || r == 'q' || r == 'p' || r == 'b' || r == 'd' || r == 't' || r == 'f' || r == 's' || r == 'h' || r == 'v' || r == 'z' || r == 'x' || r == 'r' || r == 'l' || r == 'j' || r == 'm' || r == 'n' || r == 'w' || r == 'y' || r == 'z' || r == 'C' || r == 'K' || r == 'G' || r == 'Q' || r == 'P' || r == 'B' || r == 'D' || r == 'T' || r == 'F' || r == 'S' || r == 'H' || r == 'V' || r == 'Z' || r == 'X' || r == 'R' || r == 'L' || r == 'J' || r == 'M' || r == 'N' || r == 'W' || r == 'Y' || r == 'Z'
}

func isVowel(r rune) bool {
	return r == 'a' || r == 'e' || r == 'i' || r == 'o' || r == 'u' || r == 'A' || r == 'E' || r == 'I' || r == 'O' || r == 'U'
}
