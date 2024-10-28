
// Return maximum element in the list.
// >>> MaxElement([1, 2, 3])
// 3
// >>> MaxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
// 123
func MaxElement(l []int) int {
	if len(l) == 0 {
		return 0
	}
	max := l[0]
	for i := 1; i < len(l); i++ {
		if l[i] > max {
			max = l[i]
		}
	}
	return max
}