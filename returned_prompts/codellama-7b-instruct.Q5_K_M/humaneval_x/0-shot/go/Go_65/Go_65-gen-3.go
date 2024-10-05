
// Circular shift the digits of the integer x, shift the digits right by shift
// and return the result as a string.
// If shift > number of digits, return digits reversed.
// >>> CircularShift(12, 1)
// "21"
// >>> CircularShift(12, 2)
// "12"
func CircularShift(x int,shift int) string {
	var buf bytes.Buffer
	var digits = []byte(strconv.Itoa(x))
	for i := 0; i < shift; i++ {
		digits = append(digits, digits[0])
		digits = digits[1:]
	}
	for i := len(digits) - 1; i >= 0; i-- {
		buf.WriteByte(digits[i])
	}
	return buf.String()
}
