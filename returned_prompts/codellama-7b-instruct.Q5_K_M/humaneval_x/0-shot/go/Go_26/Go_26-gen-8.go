
// From a list of integers, remove all elements that occur more than once.
// Keep order of elements left the same as in the input.
// >>> RemoveDuplicates([1, 2, 3, 2, 4])
// [1, 3, 4]
func RemoveDuplicates(numbers []int) []int {
    // Create a map to keep track of elements
    seen := make(map[int]bool)
    result := []int{}

    // Loop through the input list
    for _, num := range numbers {
        // Check if the number has been seen before
        if _, ok := seen[num]; !ok {
            // If not seen before, add it to the result
            result = append(result, num)
            // Mark it as seen
            seen[num] = true
        }
    }
    return result
}
