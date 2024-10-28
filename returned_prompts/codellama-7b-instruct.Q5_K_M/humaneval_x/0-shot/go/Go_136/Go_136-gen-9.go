
// Create a function that returns a tuple (a, b), where 'a' is
// the largest of negative integers, and 'b' is the smallest
// of positive integers in a list.
// If there is no negative or positive integers, return them as nil.
// 
// Examples:
// LargestSmallestIntegers([2, 4, 1, 3, 5, 7]) == (nil, 1)
// LargestSmallestIntegers([]) == (nil, nil)
// LargestSmallestIntegers([0]) == (nil, nil)
func LargestSmallestIntegers(lst []int) [2]interface{} {
	var largestNegative, smallestPositive *int
	for _, v := range lst {
		if v < 0 && (largestNegative == nil || v > *largestNegative) {
			largestNegative = &v
		} else if v > 0 && (smallestPositive == nil || v < *smallestPositive) {
			smallestPositive = &v
		}
	}
	return [2]interface{}{largestNegative, smallestPositive}
}

// Create a function that returns a tuple (a, b), where 'a' is
// the largest of negative integers, and 'b' is the smallest
// of positive integers in a list.
// If there is no negative or positive integers, return them as nil.
// 
// Examples:
// LargestSmallestIntegers([2, 4, 1, 3, 5, 7]) == (nil, 1)
// LargestSmallestIntegers([]) == (nil, nil)
// LargestSmallestIntegers([0]) == (nil, nil)
func LargestSmallestIntegers(lst []int) (int, int) {
	var largestNegative, smallestPositive int
	for _, v := range lst {
		if v < 0 && (largestNegative == 0 || v > largestNegative) {
			largest