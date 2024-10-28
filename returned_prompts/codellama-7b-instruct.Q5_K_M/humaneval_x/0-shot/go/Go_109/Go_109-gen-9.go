    for i := 1; i < len(arr); i++ {
        if arr[i] < arr[i-1] {
            for j := i; j >= 1; j-- {
                if arr[j] > arr[j-1] {
                    arr[j-1], arr[j] = arr[j], arr[j-1]
                    continue A
                }
            }
            return false
        }
    }
    return true
}
