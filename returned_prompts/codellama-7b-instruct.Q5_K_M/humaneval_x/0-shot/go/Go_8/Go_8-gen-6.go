
// For a given list of integers, return a list with the first half of the integers, the second half of the integers, and the sum of the first half, and the sum of the second half.
// If the length of the list is odd, the first half should include the middle element and the second half should not.
// If the length of the list is even, the first half should not include the middle element and the second half should include the middle element.
// Empty list should be handled.
// >>> SplitList([])
// ([], [], 0, 0)
// >>> SplitList([1, 2, 3, 4, 5, 6])
// ([1, 2, 3], [4, 5, 6], 6, 15)
func SplitList(numbers []int) ([]int, []int, int, int) {

