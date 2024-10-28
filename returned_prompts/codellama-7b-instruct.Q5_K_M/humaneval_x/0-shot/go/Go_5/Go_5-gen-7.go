
// Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
// >>> Intersperse([], 4)
// []
// >>> Intersperse([1, 2, 3], 4)
// [1, 4, 2, 4, 3]
func Intersperse(numbers []int, delimeter int) []int {
	var res []int
	for i, x := range numbers {
		if i > 0 {
			res = append(res, delimeter)
		}
		res = append(res, x)
	}
	return res
}

