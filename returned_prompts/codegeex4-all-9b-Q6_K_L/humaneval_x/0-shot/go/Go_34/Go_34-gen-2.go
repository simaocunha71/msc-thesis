import (
    "sort"
)

// Return sorted Unique elements in a list
// >>> Unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
// [0, 2, 3, 5, 9, 123]
func Unique(l []int) []int {
    sort.Ints(l)
    var result []int
    var last int
    for _, i := range l {
        if i != last {
            result = append(result, i)
            last = i
        }
    }
    return result
}