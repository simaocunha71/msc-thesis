
// Given two positive integers a and b, return the even digits between a
// and b, in ascending order.
// 
// For example:
// GenerateIntegers(2, 8) => [2, 4, 6, 8]
// GenerateIntegers(8, 2) => [2, 4, 6, 8]
// GenerateIntegers(10, 14) => []
func GenerateIntegers(a, b int) []int {
	var digits []int
	for i := a; i <= b; i += 2 {
		digits = append(digits, i)
	}

	return digits
}