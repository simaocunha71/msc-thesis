func RemoveDuplicates(numbers []int) []int {
	seen := map[int]bool{}
	result := []int{}
	for _, number := range numbers {
		if !seen[number] {
			seen[number] = true
			result = append(result, number)
		}
	}
	return result
}