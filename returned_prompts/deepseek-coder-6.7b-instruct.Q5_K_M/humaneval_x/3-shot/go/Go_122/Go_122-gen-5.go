    sum := 0
    for _, v := range arr[:k] {
        if len(strconv.Itoa(v)) <= 2 {
            sum += v
        }
    }
    return sum
}



