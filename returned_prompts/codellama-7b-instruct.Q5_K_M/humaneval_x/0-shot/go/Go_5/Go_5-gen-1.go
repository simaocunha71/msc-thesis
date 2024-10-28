
// Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
// >>> Intersperse([], 4)
// []
// >>> Intersperse([1, 2, 3], 4)
// [1, 4, 2, 4, 3]
func Intersperse(numbers []int, delimeter int) []int {
	if len(numbers) == 0 {
		return numbers
	}
	ret := []int{}
	for i := 0; i < len(numbers); i++ {
		ret = append(ret, numbers[i])
		if i+1 < len(numbers) {
			ret = append(ret, delimeter)
		}
	}
	return ret
}

// Split a string 's' into substrings separated by the string 'sep'
// >>> Split("a,b,c", ",")
// ["a", "b", "c"]
func Split(s, sep string) []string {
	return strings.Split(s, sep)
}

// Join all the elements of input list 'xs' into a single string.
// The separator string 'sep' is placed between elements.
// >>> Join([]int{1, 2, 3}, ",")
// "1,2,3"
func Join(xs []int, sep string) string {
	return strings.Join(IntsToString(xs), sep)
}

// Append an element 'x' to the end of input list 'xs'
// >>> Append([]int{1, 2, 3}, 4)
// [1, 2, 3, 4]
func Append(xs []int, x int) []int {
	return append(xs, x)
}

// Prepend an element 'x' to the front of input list 'xs'
// >>> Prepend([]int{1, 2, 3}, 4)
// [4, 1, 2, 3]
func Prepend(xs []int, x int) []int {
	return append([]int{x}, xs...)
}

// Return a new list with