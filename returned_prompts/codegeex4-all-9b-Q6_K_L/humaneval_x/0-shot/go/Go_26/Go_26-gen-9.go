func RemoveDuplicates(numbers []int) []int {
    seen := make(map[int]bool)
    result := make([]int, 0)
    for _, number := range numbers {
        if !seen[number] {
            result = append(result, number)
            seen[number] = true
        }
    }
    return result
}