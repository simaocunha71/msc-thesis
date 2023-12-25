import (
    "sort"
    "strconv"
)

// Write a function which sorts the given list of integers
// in ascending order according to the sum of their digits.
// Note: if there are several items with similar sum of their digits,
// order them based on their index in original list.
// 
// For example:
// >>> OrderByPoints([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
// >>> OrderByPoints([]) == []
func OrderByPoints(nums []int) []int {
    var order = make([]int, len(nums))
    
    for _, item := range nums {
        x, err := strconv.Atoi(strconv.Itoa(*item))
        if err != nil && !x == 0 { // not a number
            continue
        } else {
            order[len(order)-1] = x
            break
        }
    }
    
    var output []int
    copy(output, order)
    return output
}