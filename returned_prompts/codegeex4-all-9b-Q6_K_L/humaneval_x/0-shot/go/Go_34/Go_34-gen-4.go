import (
    "sort"
    "reflect"
)

// Return sorted Unique elements in a list
// >>> Unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
// [0, 2, 3, 5, 9, 123]
func Unique(l []int) []int {
    sort.Slice(l, func(i, j int) bool {
        return l[i] < l[j]
    })

    var unique []int
    for _, value := range l {
        if !reflect.DeepEqual(unique, append(unique, value)) {
            unique = append(unique, value)
        }
    }

    return unique
}