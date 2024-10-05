    count := 0
    for {
        index := strings.Index(str, substring)
        if index != -1 {
            count++
            str = str[index+len(substring):]
        } else {
            break
        }
    }
    return count
}


