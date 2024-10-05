func Intersperse(numbers []int, delimeter int) []int {
    length := len(numbers)
    interspersed := make([]int, 0, length*2-1)
    for i, n := range numbers {
        interspersed = append(interspersed, n)
        if i < length-1 {
            interspersed = append(interspersed, delimeter)
        }
    }
    return interspersed
}