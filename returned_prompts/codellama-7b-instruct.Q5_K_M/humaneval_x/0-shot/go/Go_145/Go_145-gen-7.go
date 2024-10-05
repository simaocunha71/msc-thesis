import (
    "sort"
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
    type pair struct {
        index int
        value int
    }
    pairs := make([]pair, len(nums))
    for i, num := range nums {
        pairs[i] = pair{i, num}
    }
    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].value != pairs[j].value {
            return pairs[i].value < pairs[j].value
        }
        return pairs[i].index < pairs[j].index
    })
    return nums
}
