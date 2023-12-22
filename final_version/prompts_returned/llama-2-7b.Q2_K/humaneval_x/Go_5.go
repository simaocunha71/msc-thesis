
// Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
// >>> Intersperse([], 4)
// []
// >>> Intersperse([1, 2, 3], 4)
// [1, 4, 2, 4, 3]
func Intersperse(numbers []int, delimeter int) []int {
	if numbers == nil || len(numbers) < 2 {
		return numbers
	} else if number, ok := numbers[0]; ok && numbers[1-ok][0:1] == 4 {
		return numbers
	}
	return append(numbers[:], delimeter, numbers[len(numbers)-ok:]...)
}
