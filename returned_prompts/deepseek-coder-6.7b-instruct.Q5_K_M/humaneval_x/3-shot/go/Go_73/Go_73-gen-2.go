    count := 0
    for i := 0; i < len(arr)/2; i++ {
        if arr[i] != arr[len(arr)-i-1] {
            count++
        }
    }
    return count
}



