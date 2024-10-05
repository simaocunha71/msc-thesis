    n := len(arr)
    left_count := 0
    right_count := 0
    count := 0
    for i, e := range arr[:n/2] {
        if e != arr[n-i-1] {
            left_count++
            count++
        }
    }
    for i, e := range arr[n/2:] {
        if e != arr[n-i-1] {
            right_count++
            count++
        }
    }

    if left_count < right_count {
        return right_count
    } else {
        return left_count
    }
}



