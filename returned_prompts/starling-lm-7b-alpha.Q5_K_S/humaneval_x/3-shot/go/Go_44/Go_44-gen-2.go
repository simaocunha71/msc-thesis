    if x == 0 {
        return "0"
    }
    result := make([]rune, 0)
    for x != 0 {
        result = append(result, rune(x%base + '0'))
        x /= base
    }
    return string(result)
}



