func IsPalindrome(text string) bool {
	return text == reverse(text)
}

func reverse(text string) string {
	var reversed string
	for i := len(text) - 1; i >= 0; i-- {
		reversed += string(text[i])
	}
	return reversed
}