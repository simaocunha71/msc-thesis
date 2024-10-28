import (
    "sort"
)

// Return sorted Unique elements in a list
// >>> Unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
// [0, 2, 3, 5, 9, 123]
func Unique(l []int) []int {

    sort.Ints(l)
    m := make([]int, 0)
    for _, v := range l {
        if !contains(m, v) {
            m = append(m, v)
        }
    }
    return m
}
