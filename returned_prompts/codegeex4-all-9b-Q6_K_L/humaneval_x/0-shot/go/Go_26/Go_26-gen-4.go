func RemoveDuplicates(numbers []int) []int {
    set := map[int]bool{}
    result := []int{}
    for _, num := range numbers {
        if _, ok := set[num]; !ok {
            set[num] = true
            result = append(result, num)
        }
    }
    return result
}