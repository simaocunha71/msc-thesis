
// Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
// >>> Intersperse([], 4)
// []
// >>> Intersperse([1, 2, 3], 4)
// [1, 4, 2, 4, 3]
func Intersperse(numbers []int, delimeter int) []int {
    var result []int
    for i, v := range numbers {
        if i > 0 {
            result = append(result, delimeter)
        }
        result = append(result, v)
    }
    return result
}

B:

// Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
// >>> Intersperse([], 4)
// []
// >>> Intersperse([1, 2, 3], 4)
// [1, 4, 2, 4, 3]
func Intersperse(numbers []int, delimeter int) []int {
    var result []int
    for i, v := range numbers {
        if i > 0 {
            result = append(result, delimeter)
        }
        result = append(result, v)
    }
    return result
}

C:

// Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
// >>> Intersperse([], 4)
// []
// >>> Intersperse([1, 2, 3], 4)
// [1, 4, 2, 4, 3]
func Intersperse(numbers []int, delimeter int) []int {
    var result []int
    for i, v := range numbers {
        if i > 0 {
            result = append(result, delimeter)
        }
        result = append(result, v)
    }
    return result
}

D:

// Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
// >>> Intersperse([], 4)
// []
// >>> Intersperse([1, 2, 3], 4)
// [1,