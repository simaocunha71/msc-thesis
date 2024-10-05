    result := 0
    l := len(arr)
    for i := 0; i < l/2; i++ {
        if arr[i] != arr[l-i-1]{
            result += 1
        }
    }
    return result
}



