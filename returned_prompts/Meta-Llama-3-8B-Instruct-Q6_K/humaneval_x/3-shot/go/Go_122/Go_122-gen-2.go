    sum := 0
    for i := 0; i < k; i++ {
        num_str := strconv.Itoa(arr[i])
        if len(num_str) <= 2 {
            sum += arr[i]
        }
    }
    return sum
}