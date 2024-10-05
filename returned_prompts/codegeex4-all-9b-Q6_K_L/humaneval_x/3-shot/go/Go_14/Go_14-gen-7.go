    result := make([]string, 0)
    for i:=0; i < len(str); i++ {
        result = append(result, str[0:i+1])
    }
    return result
}

