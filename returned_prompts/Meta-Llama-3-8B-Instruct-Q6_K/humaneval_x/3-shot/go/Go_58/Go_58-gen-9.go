    set1 := make(map[int]bool)
    set2 := make(map[int]bool)
    for _, v := range l1 {
        set1[v] = true
    }
    for _, v := range l2 {
        set2[v] = true
    }

    var result []int
    for k := range set1 {
        if set2[k] {
            result = append(result, k)
        }
    }
    sort.Ints(result)
    return result
}
}  // This is the end of the code. It is written in Go language. The code includes four functions: 
// 1. HasCloseElements: Check if in given list of numbers, are any two numbers closer to each other than given threshold.
// 2. SeparateParenGroups: Separate groups of nested parentheses from a given string.
// 3. TruncateNumber: Given a positive floating point number, it can be decomposed into and integer part (largest integer smaller than given number) and decimals (leftover part always smaller than 1). Return the decimal part of the number.
// 4. Common: Return sorted unique Common elements for two lists.
}  // This is the end of the comments.  The code is written in Go language.  The code includes four functions: 
// 1. HasCloseElements: Check if in given list of numbers, are any two numbers closer to each other than given threshold.
// 2. SeparateParenGroups: Separate groups of nested parentheses from a given string.
// 3. TruncateNumber: Given a positive floating point number, it can be decomposed into and integer part (largest integer smaller than given number) and decimals (leftover part always smaller than 1). Return the decimal part of the number.
// 4. Common: Return sorted unique Common elements for two lists.  // This is the end of the code.  The code is written in Go language.  The code includes four functions: 
// 1. HasCloseElements: Check if in given list of numbers, are any two numbers closer to each other than given threshold.
// 2. SeparateParenGroups: Separate groups of nested parentheses from a given string.
// 3. TruncateNumber: Given a positive floating point number, it can be decomposed into and integer part (largest integer smaller than given number) and decimals (leftover part always smaller than 1). Return the decimal part of the number.
// 4. Common