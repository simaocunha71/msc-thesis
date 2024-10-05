
	chars := []rune(s)
	isLetter := false
	for i := 0; i < len(chars); i++ {
		if unicode.IsLetter(chars[i]) {
			isLetter = true
			if unicode.IsLower(chars[i]) {
				chars[i] = unicode.ToUpper(chars[i])
			} else {
				chars[i] = unicode.ToLower(chars[i])
			}
		}
	}
	if !isLetter {
		for i := 0; i < len(chars)/2; i++ {
			chars[i], chars[len(chars)-1-i] = chars[len(chars)-1-i], chars[i]
		}
	}
	return string(chars)
}

// The function Solve(s) reverses the case of all letters in the string s and checks if the string contains any letters.
// If it contains no letters, it reverses the string.
// If the string contains letters, it checks each character in the string.
// If it finds a letter, it changes the case of the letter and sets the variable isLetter to true.
// After going through all characters, if isLetter is still false, it reverses the string.
// The function finally returns the modified string.
// The complexity of the function is O(n), where n is the length of the string.
func main()  {
	fmt.Println(Solve("1234")) // "4321"
	fmt.Println(Solve("ab")) // "AB"
	fmt.Println(Solve("#a@C")) // "#A@c"
}


































































































