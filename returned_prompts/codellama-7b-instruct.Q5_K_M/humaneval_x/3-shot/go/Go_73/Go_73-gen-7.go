    var min_count int = 0
    for i := 0; i < len(arr); i++ {
        var count int = 0
        for j := 0; j < len(arr); j++ {
            if arr[i] != arr[j]{
                count += 1
            }
        }
        if count < min_count {
            min_count = count
        }
    }
    return min_count
}



