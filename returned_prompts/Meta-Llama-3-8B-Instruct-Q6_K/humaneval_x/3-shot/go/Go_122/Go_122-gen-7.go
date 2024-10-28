    sum := 0
    for i := 0; i < k; i++ {
        s := strconv.Itoa(arr[i])
        if len(s) <= 2 {
            sum += arr[i]
        }
    }
    return sum
}