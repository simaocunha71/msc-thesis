
// Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
// >>> Intersperse([], 4)
// []
// >>> Intersperse([1, 2, 3], 4)
// [1, 4, 2, 4, 3]
func Intersperse(numbers []int, delimeter int) []int {
    // We need to create a new list of the same length as the original,
    // with the delimiters inserted
    var length = len(numbers)
    if length == 0 {
        return numbers
    }

    // Create a list that is one element longer than the original, with
    // the delimiters inserted
    var newList = make([]int, length + length - 1)

    // Copy the original list into the new list, inserting the delimiters
    // as we go
    for i := 0; i < length; i++ {
        newList[i*2] = numbers[i]
        if i < length - 1 {
            newList[i*2 + 1] = delimeter
        }
    }

    // Return the new list
    return newList
}
