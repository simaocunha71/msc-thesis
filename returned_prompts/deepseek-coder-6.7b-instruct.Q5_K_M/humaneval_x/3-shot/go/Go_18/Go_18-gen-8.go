    count := 0
    for {
        index := strings.Index(str, substring)
        if index == -1 {
            break
        }
        count += 1
        str = str[index+len(substring):]
    }
    return count
}



