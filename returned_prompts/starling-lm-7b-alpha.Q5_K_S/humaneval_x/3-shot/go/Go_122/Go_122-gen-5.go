    result := 0
    for _, i := range arr[:k] {
        if len(strconv.Itoa(i)) <= 2 {
            result += i
        }
    }
    return result
}



