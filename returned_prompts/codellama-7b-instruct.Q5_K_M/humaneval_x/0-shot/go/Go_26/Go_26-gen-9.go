
// From a list of integers, remove all elements that occur more than once.
// Keep order of elements left the same as in the input.
// >>> RemoveDuplicates([1, 2, 3, 2, 4])
// [1, 3, 4]
func RemoveDuplicates(numbers []int) []int {

    // Create a map of all elements and their counts
    elementCounts := make(map[int]int)
    for _, element := range numbers {
        elementCounts[element]++
    }

    // Iterate over the input list and only keep elements that have a count of 1
    result := []int{}
    for _, element := range numbers {
        if elementCounts[element] == 1 {
            result = append(result, element)
        }
    }
    return result
}

