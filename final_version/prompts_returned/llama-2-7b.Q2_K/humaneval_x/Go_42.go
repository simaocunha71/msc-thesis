
// Return list with elements incremented by 1.
// >>> IncrList([1, 2, 3])
// [2, 3, 4]
// >>> IncrList([5, 3, 5, 2, 3, 3, 9, 0, 123])
// [6, 4, 6, 3, 4, 4, 10, 1, 124]
func IncrList(l []int) []int {
	res := make([]int, len(l))
	for i, v := range l {
		res[i+1:] = append([]int{}, res[i:])
		v += 1
		res = append(res[:], v)
	}
	return res
}