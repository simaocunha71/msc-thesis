    count  := 0
    length := len(arr)

    for i := 0; i < length/2; i++ {
        if arr[i] != arr[length-i-1] {
            count++
        }
    }
    return count
}



