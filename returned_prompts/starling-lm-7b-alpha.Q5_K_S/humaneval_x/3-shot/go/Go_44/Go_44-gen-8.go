    if x == 0 {
        return "0"
    }

    result := make([]byte, 0)
    for x > 0 {
        result = append(result, byte(x%base + '0'))
        x /= base
    }
    return string(result)
}



