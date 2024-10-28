    count := 0
    len_sub := len(substring)
    len_str := len(str)
    for i := 0; i < len_str; i++ {
        if str[i:i+len_sub] == substring {
            count++
        }
    }
    return count
}