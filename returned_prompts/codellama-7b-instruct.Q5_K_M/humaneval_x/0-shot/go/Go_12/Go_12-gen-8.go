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
	max := strings[0]
	for _, s := range strings {
		if len(s) > len(max) {
			max = s
		}
	}
	return max
}

// Out of list of integers, return the largest one. Return nil in case the input list is empty.
// >>> Max([])
// nil
// >>> Max([1])
// 1
// >>> Max([1, 2, 3])
// 3
func Max(numbers []int) interface{} {
	if len(numbers) == 0 {
		return nil
	}
	max := numbers[0]
	for _, n := range numbers {
		if n > max {
			max = n
		}
	}
	return max
}

// Out of list of integers, return the smallest one. Return nil in case the input list is empty.
// >>> Min([])
// nil
// >>> Min([1])
// 1
// >>> Min([1, 2, 3])
// 1
func Min(numbers []int) interface{} {
	if len(numbers) == 0 {
		return nil
	}
	min := numbers[0]
	for _, n := range numbers {
		if n < min {
			min = n
		}
	}
	return min
}

// Out of list of strings, return the Shortest one. Return the first one in case of multiple
// strings of the same length. Return nil in case the input list is empty.
// >>> Shortest([])
// nil
// >>> Shortest(['a', 'b', 'c'])
// 'a'
