    count := 0
    for {
        pos := strings.Index(str, substring)
        if pos == -1 {
            break
        }
        count++
        str = str[pos+1:]
    }
    return count
}

