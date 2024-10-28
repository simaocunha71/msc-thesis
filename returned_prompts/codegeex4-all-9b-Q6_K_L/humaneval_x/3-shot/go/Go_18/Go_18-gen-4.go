    count := 0
    length := len(substring)
    for i := 0; i < len(str); i++ {
        if str[i:i+length] == substring {
            count++
        }
    }
    return count
}



