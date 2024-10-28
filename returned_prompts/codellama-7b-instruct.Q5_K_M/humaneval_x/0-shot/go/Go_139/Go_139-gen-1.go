
// The solution is to use a recursive function that will take the remaining
// number of factorials to calculate and a running product of the result.
func SpecialFactorial(n int) int {

	// If the number of factorials to calculate is 0, return the product.
	if n == 0 {
		return 1
	}

	// Calculate the remaining factorials.
	result := SpecialFactorial(n-1)

	// Multiply the result by the current number.
	result *= n

	// Return the result.
	return result
}

}