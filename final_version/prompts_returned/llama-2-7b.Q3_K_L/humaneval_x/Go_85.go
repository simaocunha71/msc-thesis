
// Given a non-empty list of integers lst. Add the even elements that are at odd indices..
// 
// Examples:
// Add([4, 2, 6, 7]) ==> 2
func Add(lst []int) int {
	if len(lst) == 0 {
		return 0
	}

	var i = 0
	for ; i < len(lst); i += 2 {
		if i%2 == 1 {
			add := lst[i] + lst[i+1]
			if add > 9 {
				return 0
			}
			lst[i/2+1] += add % 10
			lst[i/2+1] = (lst[i/2+1] + 10) % 10
		}
	}

	return len(lst)
}