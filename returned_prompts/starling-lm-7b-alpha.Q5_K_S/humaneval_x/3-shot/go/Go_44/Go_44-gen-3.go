    if x == 0 {
        return "0"
    }
    result := make([]rune, 0)
    for x > 0 {
        result = append(result, []rune(strconv.Itoa(x % base))...)
        x /= base
    }
    for i, v := range result {
        result[i] -= '0'
    }
    return string(result)
}



