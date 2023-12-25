
// Given a non-empty list of integers lst. Add the even elements that are at odd indices..
// 
// Examples:
// Add([4, 2, 6, 7]) ==> 2
func Add(lst []int) int {
	if len(lst) == 0 {
		return 0;
	} else if len(lst) % 2 != 0 {
		return 1;
	}
	num := -1;
	for i, v := range lst {
		if i%2 == 1 && v%2 == 0 {
			if num < 0 || len(lst) <= num {
				num = i + 1;
			} else if num > (len(lst))/2 {
				return num - (len(lst)/2) - 1;
			}
		}
	}
	return 0;
}
