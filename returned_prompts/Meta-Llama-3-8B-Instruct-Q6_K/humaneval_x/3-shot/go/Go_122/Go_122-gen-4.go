    sum := 0
    for i := 0; i < k && i < len(arr); i++ {
        if len(strconv.FormatInt(int64(arr[i]), 10)) <= 2 {
            sum += arr[i]
        }
    }
    return sum
}