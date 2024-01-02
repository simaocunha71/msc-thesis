
// Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
// >>> Intersperse([], 4)
// []
// >>> Intersperse([1, 2, 3], 4)
// [1, 4, 2, 4, 3]
func Intersperse(numbers []int, delimeter int) []int {
    if len(numbers) == 0 {
        return numbers
    }
    
    output := make([]int,len(numbers)+1)
    copy(output,numbers)
    for idx,element := range output {
        
        if element != delimeter {
            output[idx+1] = element
        } else {
            output[idx+1] = 0
        }
    
    }
    return output
}