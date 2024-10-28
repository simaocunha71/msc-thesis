    sort.Slice(arr, func(i, j int) bool {
        return arr[i] > arr[j]
    })
    return arr[:k]
}




func Maximum(arr []int, k int) []int {
    arr = append(arr[:k], arr[k:]...)
    sort.Ints(arr)
    return arr[:k]
}




func Maximum(arr []int, k int) []int {
    arr = append(arr[:k], arr[k:]...)
    sort.Slice(arr, func(i, j int) bool {
        return arr[i] > arr[j]
    })
    return arr[:k]
}




func Maximum(arr []int, k int) []int {
    arr = append(arr[:k], arr[k:]...)
    sort.Ints(arr[:k])
    return arr[:k]
}




func Maximum(arr []int, k int) []int {
    arr = append(arr[:k], arr[k:]...)
    sort.Slice(arr[:k], func(i, j int) bool {
        return arr[i] > arr[j]
    })
    return arr[:k]
}




func Maximum(arr []int, k int) []int {
    arr = append(arr[:k], arr[k:]...)
    sort.Sort(sort.Reverse(arr[:k]))
    return arr[:k]
}




func Maximum(arr []int, k int) []int {
    arr = append(arr[:k], arr[k:]...)
    sort.Slice(arr[:k], func(i, j int) bool {
        return arr[i] > arr[j]
    })
    sort.Slice(arr[:k], func(i, j int) bool {
        return arr[i] < arr[j]
    })
    return arr[:k]
}




func Maximum(arr []int, k int) []int {
    arr = append(arr[:k], arr[k:]...)
    sort