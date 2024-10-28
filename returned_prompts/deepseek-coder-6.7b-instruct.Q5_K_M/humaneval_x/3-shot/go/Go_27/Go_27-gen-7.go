    result := []rune(str)
    for i := 0; i < len(result); i++ {
        if result[i] >= 'a' && result[i] <= 'z' {
            result[i] = result[i] - 32
        } else if result[i] >= 'A' && result[i] <= 'Z' {
            result[i] = result[i] + 32
        }
    }
    return string(result)
}



