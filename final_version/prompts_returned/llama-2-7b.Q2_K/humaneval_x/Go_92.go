
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
    switch x.(int), y.(int), z.(int) {
        case x: case y: case z:
            return ((x + y + z / 100.0 < z && x + y < x+y+z/100.0) || (x == int64(x)+20*z)) ;
    }
    return false;
}
