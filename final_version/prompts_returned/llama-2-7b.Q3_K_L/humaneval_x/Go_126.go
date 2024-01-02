
// Given a list of numbers, return whether or not they are sorted
// in ascending order. If list has more than 1 duplicate of the same
// number, return false. Assume no negative numbers and only integers.
// 
// Examples
// IsSorted([5]) ➞ true
// IsSorted([1, 2, 3, 4, 5]) ➞ true
// IsSorted([1, 3, 2, 4, 5]) ➞ false
// IsSorted([1, 2, 3, 4, 5, 6]) ➞ true
// IsSorted([1, 2, 3, 4, 5, 6, 7]) ➞ true
// IsSorted([1, 3, 2, 4, 5, 6, 7]) ➞ false
// IsSorted([1, 2, 2, 3, 3, 4]) ➞ true
// IsSorted([1, 2, 2, 2, 3, 4]) ➞ false
func IsSorted(lst []int) bool {
	if len(lst) < 2 {
		return true
	}
	for i := range lst {
		isIncreasing := true
		for j, v := range lst[i+1:] {
			if v > lst[i] {
				isIncreasing = false
				break
			} else if v < lst[i] {
				return false
			}
		}
		if isIncreasing {
			return true
		}
	}
	return true
}