func CanArrange(arr []int) int {
    for i := len(arr) - 1; i > 0; i-- {
        if arr[i] < arr[i-1] {
            return i-1
        }
    }
    return -1
}