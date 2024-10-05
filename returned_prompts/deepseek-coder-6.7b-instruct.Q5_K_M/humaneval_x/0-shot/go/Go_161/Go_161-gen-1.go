
	count := 0
	for _, c := range s {
		if unicode.IsLetter(c) {
			count++
		}
	}
	if count == 0 {
		return reverse(s)
	}

B:

	b := []byte(s)
	for i, c := range b {
		if unicode.IsLetter(rune(c)) {
			if unicode.IsUpper(rune(c)) {
				b[i] = byte(unicode.ToLower(rune(c)))
			} else {
				b[i] = byte(unicode.ToUpper(rune(c)))
			}
		}
	}
	return string(b)
}

func reverse(s string) string {
	b := []byte(s)
	for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
		b[i], b[j] = b[j], b[i]
	}
	return string(b)
}


// reverse the string if there are no letters
// if there are letters, reverse the case of letters
// count the letters
// if count == 0, return reversed string
// else return string with reversed case

// convert string to bytes
// iterate over bytes
// if byte is a letter, reverse its case
// return bytes as string

// reverse function
// convert string to bytes
// swap first and last byte, then second and second last byte, and so on
// return bytes as string


// time complexity: O(n)
// space complexity: O(n)


// test cases
// "1234" -> "4321"
// "ab" -> "AB"
// "#a@C" -> "#A@c"
// "AaBbCc" -> "cCbBaA"
// "123abc" -> "cba321"
// "123ABC" -> "321abc"
// "123" -> "321"
// "" -> ""
// "