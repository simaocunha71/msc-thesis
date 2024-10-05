func SortArray(array []int) []int {
    sorted := make([]int, len(array))
    copy(sorted, array)

    if (array[0] + array[len(array)-1])%2 == 0 {
        sort.Slice(sorted, func(i, j int) bool {
            return sorted[i] > sorted[j]
        })
    } else {
        sort.Slice(sorted, func(i, j int) bool {
            return sorted[i] < sorted[j]
        })
    }

    return sorted
}
