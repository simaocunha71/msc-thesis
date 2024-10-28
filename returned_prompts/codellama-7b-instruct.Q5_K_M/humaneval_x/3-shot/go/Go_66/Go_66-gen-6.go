    result := 0
    for _, v := range x {
        if v >= 'A' && v <= 'Z' {
            result += int(v)
        }
    }
    return result
}



