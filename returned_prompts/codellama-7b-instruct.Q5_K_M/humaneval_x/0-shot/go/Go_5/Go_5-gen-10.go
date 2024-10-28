
// Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
// >>> Intersperse([], 4)
// []
// >>> Intersperse([1, 2, 3], 4)
// [1, 4, 2, 4, 3]
func Intersperse(numbers []int, delimeter int) []int {
    result := make([]int, 0, len(numbers)*2-1)
    for i := 0; i < len(numbers); i++ {
        result = append(result, numbers[i])
        if i < len(numbers)-1 {
            result = append(result, delimeter)
        }
    }
    return result
}

