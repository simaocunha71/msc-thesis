    result := []rune(str)
    for i := range result {
        if 'a' <= result[i] && result[i] <= 'z' {
            result[i] = result[i] - 'a' + 'A'
        } else if 'A' <= result[i] && result[i] <= 'Z' {
            result[i] = result[i] - 'A' + 'a'
        }
    }
    return string(result)
}


