    result := 0
    for _, v := range arr[:k] {
        if len(strconv.Itoa(v)) <= 2 {
            result += v
        }
    }
    return result
}



