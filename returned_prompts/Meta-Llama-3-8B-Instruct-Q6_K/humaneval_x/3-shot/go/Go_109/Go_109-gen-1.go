    if len(arr) == 0 {
        return true
    }
    copy := make([]int, len(arr))
    copy = arr
    sort.Ints(copy)
    for i := 0; i < len(copy); i++ {
        for j := 0; j < len(arr); j++ {
            if arr[j] != copy[i] {
                continue
            }
            if i != 0 {
                for k := 0; k < len(arr); k++ {
                    if arr[k] == copy[i-1] {
                        copy[k], copy[j] = copy[j], copy[k]
                        break
                    }
                }
            }
            return true
        }
    }
    return false
}