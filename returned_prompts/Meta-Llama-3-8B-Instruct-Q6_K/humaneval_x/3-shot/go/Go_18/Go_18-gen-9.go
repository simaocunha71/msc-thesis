    count := 0
    start := 0
    for start < len(str) {
        pos := strings.Index(str[start:], substring)
        if pos == -1 {
            break
        }
        start += pos + len(substring)
        count++
    }
    return count
}