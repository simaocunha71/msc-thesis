    result := make([]string, len(str))
    for i := 0; i < len(str); i++ {
        result[i] = string(str[i])
    }
    for i := 0; i < len(str)-1; i++ {
        result[i] += string(str[i+1])
    }
    return result
}



