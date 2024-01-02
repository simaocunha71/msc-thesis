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
    sort.Ints(lst)
    for i := 1; i <= len(lst); i++ {
        if lst[i-1]*2 < lst[i]*2 && (i%3 != 0 || i == len(lst)-1) {
            tmp := lst[i]
            lst[i] = lst[len(lst)/2] // even position
            lst[len(lst)/2] = tmp      // odd position
        }
    }
    return lst
}