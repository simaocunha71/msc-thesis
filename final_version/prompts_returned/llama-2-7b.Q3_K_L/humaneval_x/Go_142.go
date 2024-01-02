import (
    "math"
)

// This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a
// multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not
// change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries.
// 
// Examples:
// For lst = [1,2,3] the output should be 6
// For lst = []  the output should be 0
// For lst = [-1,-5,2,-1,-5]  the output should be -126
func SumSquares(lst []int) int {
    sum := 0
    for _, v := range lst {
        if (len(lst)/3 == math.Floor(len(lst)/3)) &&
            ((v%3)*(v%3) != 1 || (v%4)*(v%4) != 1) {
            sum += v * v // Cube
        } else {
            sum += v * v // Square
        }
    }
    return sum
}