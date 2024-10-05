
// A simple program which should return the value of x if n is
// a prime number and should return the value of y otherwise.
// 
// Examples:
// for XOrY(7, 34, 12) == 34
// for XOrY(15, 8, 5) == 5
func XOrY(n, x, y int) int {
	if n%2 == 0 {
		return y
	}
	return x
}
