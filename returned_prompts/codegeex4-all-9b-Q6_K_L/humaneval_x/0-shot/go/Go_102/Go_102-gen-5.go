func ChooseNum(x, y int) int {
	if x % 2 == 0 {
		return x
	} else if x == y {
		return -1
	}
	return ChooseNum(x+1, y)
}