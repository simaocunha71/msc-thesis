import (
	"sort"
)

// Return sorted Unique elements in a list
// >>> Unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
// [0, 2, 3, 5, 9, 123]
func Unique(l []int) []int {
    sort.Ints(l)
    i := 0
    for j := 1; j < len(l); j++ {
        if l[i] != l[j] {
            i++
            l[i] = l[j]
        }
    }
    return l[:i+1]
}