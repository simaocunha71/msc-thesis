
// From a list of integers, remove all elements that occur more than once.
// Keep order of elements left the same as in the input.
// >>> RemoveDuplicates([1, 2, 3, 2, 4])
// [1, 3, 4]
func RemoveDuplicates(numbers []int) []int {
    seen := map[int]bool{}
    result := []int{}
    for _, num := range numbers {
        if !seen[num] {
            seen[num] = true
            result = append(result, num)
        }
    }
    return result
}

B:

// From a list of integers, remove all elements that occur more than once.
// Keep order of elements left the same as in the input.
// >>> RemoveDuplicates([1, 2, 3, 2, 4])
// [1, 3, 4]
func RemoveDuplicates(numbers []int) []int {
    return numbers[:len(numbers):len(numbers)]
}

C:

// From a list of integers, remove all elements that occur more than once.
// Keep order of elements left the same as in the input.
// >>> RemoveDuplicates([1, 2, 3, 2, 4])
// [1, 3, 4]
func RemoveDuplicates(numbers []int) []int {
    var result []int
    for i := 0; i < len(numbers); i++ {
        if i == 0 || numbers[i] != numbers[i-1] {
            result = append(result, numbers[i])
        }
    }
    return result
}
