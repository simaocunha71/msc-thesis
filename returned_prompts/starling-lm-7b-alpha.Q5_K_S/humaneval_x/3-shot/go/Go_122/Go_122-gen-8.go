    result := 0
    for i := 0; i < k; i++ {
        result += arr[i]
        if len(strconv.Itoa(arr[i])) > 2 {
            return result
        }
    }
    return result
}



