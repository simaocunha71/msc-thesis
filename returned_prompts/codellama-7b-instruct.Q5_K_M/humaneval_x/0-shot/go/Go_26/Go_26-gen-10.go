
// From a list of integers, remove all elements that occur more than once.
// Keep order of elements left the same as in the input.
// >>> RemoveDuplicates([1, 2, 3, 2, 4])
// [1, 3, 4]
func RemoveDuplicates(numbers []int) []int {
	// map[number]index
	m := make(map[int]int)
	// index of the first occurrence of the number
	for i, num := range numbers {
		// if number is not seen yet
		if _, ok := m[num]; !ok {
			// save number's index
			m[num] = i
		}
	}
	// return numbers that have not been seen before
	res := make([]int, 0, len(numbers))
	for _, num := range numbers {
		// if number is seen first time
		if i, ok := m[num]; ok && i == 0 {
			res = append(res, num)
		}
	}
	return res
}
