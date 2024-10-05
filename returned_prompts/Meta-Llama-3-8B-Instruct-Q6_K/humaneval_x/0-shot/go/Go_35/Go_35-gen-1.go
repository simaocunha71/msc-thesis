    // return the maximum element in the list
    // we can use the built-in sort function and return the last element
    // or we can use a loop to find the maximum
    // we will use the first approach
    var max int
    for _, v := range l {
        if v > max {
            max = v
        }
    }
    return max
}
// test the function
fmt.Println(MaxElement([]int{1, 2, 3})) // 3
fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})) // 123
// test the function with empty list
fmt.Println(MaxElement([]int{})) // error: runtime error: index out of range

