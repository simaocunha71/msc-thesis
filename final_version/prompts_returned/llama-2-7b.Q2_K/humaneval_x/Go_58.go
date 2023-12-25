import (
    "sort"
)

// Return sorted unique Common elements for two lists.
// >>> Common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
// [1, 5, 653]
// >>> Common([5, 3, 2, 8], [3, 2])
// [2, 3]
func Common(l1 []int,l2 []int) []int {
    if len(l1) == 0 || len(l1) == 1 && len(l2) > 0 {
        return append([]int{}, l1...)
    }

    // get unique elements in both lists
    uniq1 := make(map[int]bool, len(l1))
    for _, i := range l1 {
        uniq1[i] = true
    }

    uniq2 := make(map[int]bool, len(l2))
    for _, j := range l2 {
        if uniq2[j] == false {
            uniq2[j] = true
        }
    }

    uniq := make([]int, 0, len(uniq1) + len(uniq2))
    // put unique elements in both lists to uniq and sort it
    for i, v := range l1 {
        if _, ok := uniq[v]; ok == false {
            uniq = append([]int{}, v...)
            sort.Sort(sort.Reverse(sort.IntSlice(len(uniq))))
        }
    }
    for j, v := range l2 {
        if _, ok := uniq[v]; ok == false && len(uninq) > 0 {
            continue
        }
        if len(j) > len(l1) { // this is last index of l2 and l1.
            break
        } else { // if not l2's first element, replace the next one by this elements from uniq list.
            j++