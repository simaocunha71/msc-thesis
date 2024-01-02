import (
    "fmt"
    "sort"
)

// In this Kata, you have to sort an array of non-negative integers according to
// number of ones in their binary representation in ascending order.
// For similar number of ones, sort based on decimal value.
// 
// It must be implemented like this:
// >>> SortArray([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
// >>> SortArray([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
// >>> SortArray([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
func SortArray(arr []int) []int {
    // write your code here
    sort.Ints(arr)
    newArr := make([]int, len(arr))
    for i, number := range arr {
        if number >= 0 {
            newArr[i] = int(number)
        } else {
            newArr[i] = -1 * number
        }
    }

    return newArr
}
func main() {
    fmt.Printf("SortArray([%v]) == [%v]\n", arr, sorted)
    fmt.Println(arr)
}