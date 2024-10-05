    count := 0
    for {
        index := strings.Index(str, substring)
        if index != -1 {
            count += 1
            str = str[index+len(substring):]
        } else {
            break
        }
    }
    return count
}



