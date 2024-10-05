    result := make([]rune, 0)
    if x < 0 {
        result = append(result, '-')
        x = -x
    }
    for x > 0 {
        result = append(result, rune(x%base + '0'))
        x /= base
    }
    return string(result)
}



