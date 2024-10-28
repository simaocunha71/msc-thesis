
// From a list of integers, remove all elements that occur more than once.
// Keep order of elements left the same as in the input.
// >>> RemoveDuplicates([1, 2, 3, 2, 4])
// [1, 3, 4]
func RemoveDuplicates(numbers []int) []int {

	// Create a map of elements and their counts.
	counts := make(map[int]int)
	for _, n := range numbers {
		counts[n]++
	}

	// Create a list of unique elements.
	unique := make([]int, 0, len(numbers))
	for n, count := range counts {
		if count == 1 {
			unique = append(unique, n)
		}
	}

	return unique
}

func main() {
	fmt.Println(RemoveDuplicates([]int{1, 2, 3, 2, 4}))
}

