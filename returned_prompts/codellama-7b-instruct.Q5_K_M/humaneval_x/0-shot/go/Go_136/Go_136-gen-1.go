
// Create a function that returns a tuple (a, b), where 'a' is
// the largest of negative integers, and 'b' is the smallest
// of positive integers in a list.
// If there is no negative or positive integers, return them as nil.
// 
// Examples:
// LargestSmallestIntegers([2, 4, 1, 3, 5, 7]) == (nil, 1)
// LargestSmallestIntegers([]) == (nil, nil)
// LargestSmallestIntegers([0]) == (nil, nil)
func LargestSmallestIntegers(lst []int) [2]interface{}{
	negative := false
	positive := false
	var largestNegative *int
	var smallestPositive *int
	for i := range lst {
		if lst[i] < 0 {
			if !negative {
				negative = true
				largestNegative = &lst[i]
			} else {
				if lst[i] > *largestNegative {
					*largestNegative = lst[i]
				}
			}
		}
		if lst[i] > 0 {
			if !positive {
				positive = true
				smallestPositive = &lst[i]
			} else {
				if lst[i] < *smallestPositive {
					*smallestPositive = lst[i]
				}
			}
		}
	}
	if negative {
		return [2]interface{}{*largestNegative, nil}
	}
	if positive {
		return [2]interface{}{nil, *smallestPositive}
	}
	return [2]interface{}{nil, nil}
}

