    var sum int = 0

    for i := 0; i < k; i++ {
        str_val := strconv.Itoa(arr[i])
        if len(str_val) <= 2 {
            sum += arr[i]
        }
    }
    return sum
}



