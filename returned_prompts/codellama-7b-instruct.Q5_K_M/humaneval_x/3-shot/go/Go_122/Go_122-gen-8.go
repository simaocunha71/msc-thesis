    result := 0
    for i := 0; i < k; i++ {
        var element_str string = strconv.Itoa(arr[i])
        if len(element_str) <= 2 {
            result += arr[i]
        }
    }
    return result
}



