func ChooseNum(x, y int) int {
    // Make sure x is always the smaller number
    if x > y {
        x, y = y, x
    }
    // Iterate through the range from x to y
    for i := x; i <= y; i++ {
        // Check if the number is even
        if i%2 == 0 {
            return i
        }
    }
    // If no even number is found, return -1
    return -1
}