    sum := 0
    for _, v := range arr {
        if len(strconv.Itoa(v)) <= 2 {
            sum += v
        }
        if k == 0 {
            break
        }
        k--
    }
    return sum
}

