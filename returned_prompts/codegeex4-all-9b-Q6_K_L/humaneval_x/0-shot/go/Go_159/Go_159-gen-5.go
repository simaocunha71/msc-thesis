func Eat(number, need, remaining int) []int {
	if need >= remaining {
		return []int{number + remaining, 0}
	}
	return []int{number + need, remaining - need}
}