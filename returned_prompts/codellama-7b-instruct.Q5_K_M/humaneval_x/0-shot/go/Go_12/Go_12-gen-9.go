// Out of list of strings, return the Longest one. Return the first one in case of multiple
// strings of the same length. Return nil in case the input list is empty.
// >>> Longest([])
// nil
// >>> Longest(['a', 'b', 'c'])
// 'a'
// >>> Longest(['a', 'bb', 'ccc'])
// 'ccc'
func Longest(strings []string) interface{}{
	if len(strings) == 0 {
		return nil
	}
	var longestLen int
	var longest string
	for _, s := range strings {
		if len(s) > longestLen {
			longestLen = len(s)
			longest = s
		}
	}
	return longest
}

// Out of list of integers, return the sum of all integers.
// >>> Sum([])
// 0
// >>> Sum([1])
// 1
// >>> Sum([1, 2, 3])
// 6
// >>> Sum([1, 2, 3, -4])
// 2
func Sum(nums []int) int {
	var sum int
	for _, num := range nums {
		sum += num
	}
	return sum
}

// Out of list of strings, return the count of all strings.
// >>> Count([])
// 0
// >>> Count(['a'])
// 1
// >>> Count(['a', 'b', 'c'])
// 3
func Count(strings []string) int {
	return len(strings)
}

// Out of list of integers, return the average of all integers.
// >>> Average([])
// 0
// >>> Average([1])
// 1
// >>> Average([1, 2, 3])
// 2
// >>> Average([1, 2, 3, -4])
// -1
func Average(nums []int) float64 {
	return float64(Sum(nums)) / float64(Count(nums))
}