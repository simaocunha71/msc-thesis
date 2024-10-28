
// Circular shift the digits of the integer x, shift the digits right by shift
// and return the result as a string.
// If shift > number of digits, return digits reversed.
// >>> CircularShift(12, 1)
// "21"
// >>> CircularShift(12, 2)
// "12"
func CircularShift(x int,shift int) string {
	xStr := strconv.Itoa(x)
	xLen := len(xStr)
	if shift > xLen {
		return strings.Reverse(xStr)
	}
	shiftLen := shift
	if shiftLen >= xLen {
		shiftLen = xLen - 1
	}
	first := xStr[xLen-1-shiftLen:]
	second := xStr[:xLen-shiftLen]
	return second + first
}
