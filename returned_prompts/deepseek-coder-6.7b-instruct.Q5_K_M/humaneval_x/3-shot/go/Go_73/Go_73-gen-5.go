    changes := 0
    for i:=0; i<len(arr)/2; i++ {
        j := len(arr)-1-i
        if arr[i] != arr[j] {
            changes++
        }
    }
    return changes
}



