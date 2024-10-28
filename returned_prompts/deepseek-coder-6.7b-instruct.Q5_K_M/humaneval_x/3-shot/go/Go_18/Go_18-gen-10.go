    count := 0
    for  {
        index := strings.Index(str, substring)
        if index != 0 {
            break
        }
        count++
        str = str[index+1:]
    }
    return count
}



