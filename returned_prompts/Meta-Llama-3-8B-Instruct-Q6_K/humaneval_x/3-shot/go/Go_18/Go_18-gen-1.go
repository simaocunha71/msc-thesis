    count := 0
    start := 0
    for start < len(str) {
        pos := strings.Index(str[start:], substring)
        if pos == -1 {
            break
        }
        count++
        start += pos + len(substring)
    }
    return count
}