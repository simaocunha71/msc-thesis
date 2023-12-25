
// The Brazilian factorial is defined as:
// brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
// where n > 0
// 
// For example:
// >>> SpecialFactorial(4)
// 288
// 
// The function will receive an integer as input and should return the special
// factorial of this integer.
func SpecialFactorial(n int) int {
	if n < 0 {
		return 0
	}
	count := 1
	for i := n; i > 0 ; i -= count {
		count *= i
	}
	return count
}
