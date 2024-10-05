    count := 0
    start := 0
    for {
        pos := strings.Index(str[start:], substring)
        if pos == -1 {
            break
        }
        count++
        start += pos + len(substring)
    }
    return count
} 