
// Return a greatest common divisor of two integers a and b
// >>> GreatestCommonDivisor(3, 5)
// 1
// >>> GreatestCommonDivisor(25, 15)
// 5
func GreatestCommonDivisor(a int,b int) int{

	// If one of the arguments is zero, return the other
	if a == 0 {
		return b
	}
	if b == 0 {
		return a
	}

	// Find the greatest common divisor of the lower numbers
	// and add the larger number until it is divided evenly
	for {
		a, b = b, a % b
		if b == 0 {
			return a
		}
	}
}