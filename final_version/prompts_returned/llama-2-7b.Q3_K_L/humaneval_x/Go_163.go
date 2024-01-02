
// Given two positive integers a and b, return the even digits between a
// and b, in ascending order.
// 
// For example:
// GenerateIntegers(2, 8) => [2, 4, 6, 8]
// GenerateIntegers(8, 2) => [2, 4, 6, 8]
// GenerateIntegers(10, 14) => []
func GenerateIntegers(a, b int) []int {
	var list []int
	for i := a; i <= b; i++ {
		if a%i == 0 && b%i == 0 && i != 0 && i%2 == 1{
			list = append(list, i)
		}
	}
	return list
}
