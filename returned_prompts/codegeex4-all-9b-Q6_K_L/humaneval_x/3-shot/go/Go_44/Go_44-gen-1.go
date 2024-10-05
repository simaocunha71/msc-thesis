    result := ""
    for x > 0 {
        result = strconv.Itoa(x%base) + result
        x = x / base
    }
    return result
}

