    count := 0
    for i := 0; i < len(str); i++ {
        if strings.HasPrefix(str[i:], substring) {
            count++
        }
    }
    return count
}



