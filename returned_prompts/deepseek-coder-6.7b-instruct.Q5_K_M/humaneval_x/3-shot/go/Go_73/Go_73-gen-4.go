    changes := 0
    length := len(arr)
    for i := 0; i < length/2; i++ {
        if arr[i] != arr[length-1-i] {
            changes++
        }
    }
    return changes
}



