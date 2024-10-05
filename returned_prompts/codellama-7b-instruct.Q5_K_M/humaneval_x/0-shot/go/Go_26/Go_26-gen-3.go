
// From a list of integers, remove all elements that occur more than once.
// Keep order of elements left the same as in the input.
// >>> RemoveDuplicates([1, 2, 3, 2, 4])
// [1, 3, 4]
func RemoveDuplicates(numbers []int) []int {
    // Create a map to store all the numbers
    seen := make(map[int]bool)
    // Create a new list to store the numbers
    result := []int{}
    for _, number := range numbers {
        // If the number has not been seen before
        if !seen[number] {
            // Add it to the list and mark it as seen
            seen[number] = true
            result = append(result, number)
        }
    }
    return result
}
