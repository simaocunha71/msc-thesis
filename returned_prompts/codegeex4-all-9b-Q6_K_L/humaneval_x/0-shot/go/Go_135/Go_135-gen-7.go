func CanArrange(arr []int) int {
    for i, v := range arr {
        if i > 0 && v < arr[i-1] {
            return i - 1
        }
    }
    return -1
}