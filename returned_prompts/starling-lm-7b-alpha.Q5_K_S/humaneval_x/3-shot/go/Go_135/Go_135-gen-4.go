    result := -1
    max := arr[0]
    for i := 0; i < len(arr); i++ {
        if max >= arr[i] {
            if result < i {
                result = i
            }
            max = arr[i]
        }
    }
    return result
}



