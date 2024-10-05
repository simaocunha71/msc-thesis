func RemoveDuplicates(numbers []int) []int {
    seen := map[int]bool{}
    result := []int{}
    for _, n := range numbers {
        if !seen[n] {
            seen[n] = true
            result = append(result, n)
        }
    }
    return result
}