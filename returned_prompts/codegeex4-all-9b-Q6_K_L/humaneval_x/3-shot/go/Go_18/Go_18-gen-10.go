    count := 0
    len_substring := len(substring)
    for i:=0; i<len(str); i++{
        if str[i:i+len_substring] == substring{
            count += 1
        }
    }
    return count
}



