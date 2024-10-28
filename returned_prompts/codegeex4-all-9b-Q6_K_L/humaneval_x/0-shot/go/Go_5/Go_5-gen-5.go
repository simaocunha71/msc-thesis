func Intersperse(numbers []int, delimeter int) []int {
    output := make([]int, 0)
    for i, num := range numbers {
        output = append(output, num)
        if i != len(numbers) - 1 {
            output = append(output, delimeter)
        }
    }
    return output
}