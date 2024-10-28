    changes := 0
    for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
        if arr[i] != arr[j] {
            changes++
        }
    }
    return changes
}



