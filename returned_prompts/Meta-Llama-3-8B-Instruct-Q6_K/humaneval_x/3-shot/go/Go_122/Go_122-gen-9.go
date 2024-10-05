    sum := 0
    for i := 0; i < k; i++ {
        if strconv.FormatInt(int64(arr[i]), 10)[1:] == "" {
            sum += arr[i]
        }
    }
    return sum
}