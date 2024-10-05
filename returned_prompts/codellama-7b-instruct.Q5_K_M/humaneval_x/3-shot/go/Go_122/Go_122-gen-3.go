    result := 0
    for i := 0; i < k; i++ {
        temp := strconv.Itoa(arr[i])
        if len(temp) <= 2 {
            result += arr[i]
        }
    }
    return result
}



