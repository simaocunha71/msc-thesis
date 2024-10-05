import (
    "sort"
)

// Given list of integers, return list in strange order.
// Strange sorting, is when you start with the minimum value,
// then maximum of the remaining integers, then minimum and so on.
// 
// Examples:
// StrangeSortList([1, 2, 3, 4]) == [1, 4, 2, 3]
// StrangeSortList([5, 5, 5, 5]) == [5, 5, 5, 5]
// StrangeSortList([]) == []
func StrangeSortList(lst []int) []int {
    sort.Slice(lst, func(i, j int) bool {
        if lst[i] < lst[j] {
            return true
        }
        if lst[i] > lst[j] {
            return false
        }
        return i < j
    })
    return lst
}
