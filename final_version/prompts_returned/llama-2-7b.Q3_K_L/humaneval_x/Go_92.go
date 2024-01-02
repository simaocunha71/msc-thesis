
// Create a function that takes 3 numbers.
// Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
// Returns false in any other cases.
// 
// Examples
// AnyInt(5, 2, 7) ➞ true
// 
// AnyInt(3, 2, 2) ➞ false
// 
// AnyInt(3, -2, 1) ➞ true
// 
// AnyInt(3.6, -2.2, 2) ➞ false
func AnyInt(x, y, z interface{}) bool {
    xValue := x.(int)
    yValue := y.(int)
    zValue := z.(int)
    // Check each of the values to see if they are in range.
    switch {
        case (xValue >= -10 && xValue <= 9):
            return true
        default:
            return false
    }
    switch {
        case (yValue >= -10 && yValue <= 9):
            return true
        default:
            return false
    }
    switch {
        case (zValue >= -10 && zValue <= 9):
            return true
        default:
            return false
    }
}