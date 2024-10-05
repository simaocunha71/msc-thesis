func CircularShift(x int, shift int) string {
	xStr := strconv.Itoa(x)
	if shift > len(xStr) {
		return reverseString(xStr)
	}
	shift = shift % len(xStr)
	return xStr[len(xStr)-shift:] + xStr[:len(xStr)-shift]
}

func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}