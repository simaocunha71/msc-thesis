import (
    "sort"
)

// Return sorted unique Common elements for two lists.
// >>> Common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
// [1, 5, 653]
// >>> Common([5, 3, 2, 8], [3, 2])
// [2, 3]
func Common(l1 []int,l2 []int) []int {
    // Return the common elements.
    out := make([]int, len(l1), len(l1))
    for i, l := range l1 {
        ok := true
        for j, r := range l2 {
            if l == r {
                out[i] = r
                ok = false
                break
            }
        }
        if ok {
            continue
        }
    }
    return out
}
