import (
    "strconv"
)

// Given an integer. return a tuple that has the number of even and odd digits respectively.
// 
// Example:
// EvenOddCount(-12) ==> (1, 1)
// EvenOddCount(123) ==> (1, 2)
func EvenOddCount(num int) [2]int {
    var even int
    var odd int
    for _, digit := range strconv.Itoa(num) {
        if digit%2 == 0 {
            even++
        } else {
            odd++
        }
    }
    return [2]int{even, odd}
}
