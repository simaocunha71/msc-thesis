    count := 0
    for  {
        index := strings.Index(str, substring)
        if index == -1 {
            break
        }
        count++
        str = str[index+1:]
    }
    return count
}


