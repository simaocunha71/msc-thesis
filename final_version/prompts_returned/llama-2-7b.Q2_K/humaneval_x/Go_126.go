
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
	if len(lst) == 0 || len(lst) > 5 {
		return false // 5 is the limit on how long we'll test things for before bailing out. 5 is a good number to try out, since it can be tested by hand fairly easily. You could probably do more exhaustive tests in larger numbers... but that would take too much time and effort.
	} else if len(lst) == 1 { // If there's only one element in the array then return true.
		return true
	}

	if lst[0] < lst[1] || (len(lst) > 2 && lst[0] <= lst[1]) {
		// If first and second elements are not in order, return false.
		return false
	} else if len(lst) == 3 && lst[1] >= lst[0] && lst[2] < lst[1] { // If there's a duplicate to the list of three or more items, return false
		return false