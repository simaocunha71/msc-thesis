    count := 0
    pos := 0
    for pos < len(str) {
        pos = strings.Index(str[pos:], substring)
        if pos == -1 {
            break
        }
        count++
        pos += pos + len(substring)
    }
    return count
}