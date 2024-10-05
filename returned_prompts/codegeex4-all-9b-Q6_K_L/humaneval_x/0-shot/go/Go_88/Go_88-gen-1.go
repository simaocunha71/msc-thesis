import (
    "sort"
)

func SortArray(array []int) []int {
    copy := make([]int, len(array))
    copy = append(copy, array...)
    
    if len(array) == 0 {
        return array
    }
    if (array[0] + array[len(array) - 1]) % 2 == 0 {
        sort.Slice(copy, func(i, j int) bool {
            return copy[i] > copy[j]
        })
    } else {
        sort.Slice(copy, func(i, j int) bool {
            return copy[i] < copy[j]
        })
    }
    return copy
}
