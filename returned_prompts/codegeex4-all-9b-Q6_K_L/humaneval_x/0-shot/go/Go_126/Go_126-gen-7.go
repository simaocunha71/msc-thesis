func IsSorted(lst []int) bool {
    for i, v := range lst {
        if i > 0 && v < lst[i-1] {
            return false
        }
    }
    return true
}