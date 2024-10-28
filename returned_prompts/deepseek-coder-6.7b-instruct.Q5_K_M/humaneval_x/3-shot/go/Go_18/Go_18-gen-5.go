    count := 0
    for{
        index := strings.Index(str, substring)
        if index == -1{
            break
        }
        count++
        str = str[index+len(substring):]
    }
    return count
}



