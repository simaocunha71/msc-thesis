    sum := 0
    for i := 0; i < len(arr); i++ {
        if i >= k {
            break
        }
        if arr[i] <= 99 {
            sum += arr[i]
        }
    }
    return sum
}



