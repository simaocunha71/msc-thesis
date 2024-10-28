func Intersperse(numbers []int, delimeter int) []int {
    if len(numbers) < 2 {
        return numbers
    }
    result := make([]int, 0)
    for i := 0; i < len(numbers)-1; i++ {
        result = append(result, numbers[i], delimeter)
    }
    result = append(result, numbers[len(numbers)-1])
    return result
}