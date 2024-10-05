
// From a list of integers, remove all elements that occur more than once.
// Keep order of elements left the same as in the input.
// >>> RemoveDuplicates([1, 2, 3, 2, 4])
// [1, 3, 4]
func RemoveDuplicates(numbers []int) []int {
    // create a map of numbers to count of numbers
    counts := make(map[int]int)
    for _, n := range numbers {
        counts[n]++
    }
    // append the numbers that have count of 1 to result
    result := []int{}
    for n, c := range counts {
        if c == 1 {
            result = append(result, n)
        }
    }
    return result
}
