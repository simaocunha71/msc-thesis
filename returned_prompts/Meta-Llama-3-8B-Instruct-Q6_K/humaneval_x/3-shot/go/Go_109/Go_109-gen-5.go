    if len(arr) == 0 {
        return true
    }
    
    for i := 0; i < len(arr); i++ {
        for j := i + 1; j < len(arr); j++ {
            if arr[i] > arr[j] {
                return false
            }
        }
    }
    
    return true
}