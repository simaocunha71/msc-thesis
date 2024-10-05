
// Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
// >>> Intersperse([], 4)
// []
// >>> Intersperse([1, 2, 3], 4)
// [1, 4, 2, 4, 3]
func Intersperse(numbers []int, delimeter int) []int {
	if len(numbers) == 0 {
		return numbers
	}
	return append(numbers[:len(numbers)-1], append([]int{delimeter}, numbers[len(numbers)-1:]...)...)
}

