    count := 0
    index := 0
    for index < len(str) {
        index = strings.Index(str[index:], substring)
        if index == -1 {
            break
        }
        count++
        index += index + len(substring)
    }
    return count
}