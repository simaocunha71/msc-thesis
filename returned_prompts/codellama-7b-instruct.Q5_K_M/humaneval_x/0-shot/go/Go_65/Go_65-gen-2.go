
// Circular shift the digits of the integer x, shift the digits right by shift
// and return the result as a string.
// If shift > number of digits, return digits reversed.
// >>> CircularShift(12, 1)
// "21"
// >>> CircularShift(12, 2)
// "12"
func CircularShift(x int,shift int) string {

	// convert to string
	s := strconv.Itoa(x)

	// get the length of the string
	l := len(s)

	// if shift is greater than the length of the string, return the reversed digits
	if shift > l {
		return reverse(s)
	}

	// create a new string that is the original string shifted to the right
	newString := s[shift:] + s[:shift]

	// return the new string
	return newString
}

// Reverse the string
func reverse(s string) string {

	// convert the string to a rune array
	r := []rune(s)

	// reverse the array
	for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}

	// return the reversed string
	return string(r)
}