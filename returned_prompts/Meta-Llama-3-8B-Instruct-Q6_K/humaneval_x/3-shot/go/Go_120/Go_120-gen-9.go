    sort.Ints(arr)
    return arr[len(arr)-k:]
}
// or
func Maximum(arr []int, k int) []int {
    sort.Slice(arr, func(i, j int) bool {
        return arr[i] > arr[j]
    })
    return arr[:k]
}