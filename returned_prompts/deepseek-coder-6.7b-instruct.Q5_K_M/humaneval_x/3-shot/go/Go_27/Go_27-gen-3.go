    result := []rune(str)
    for i := range result {
        if result[i] >= 'a' && result[i] <= 'z' {
            result[i] = result[i] - ('a' - 'A')
        } else if result[i] >= 'A' && result[i] <= 'Z' {
            result[i] = result[i] + ('a' - 'A')
        }
    }
    return string(result)
}



