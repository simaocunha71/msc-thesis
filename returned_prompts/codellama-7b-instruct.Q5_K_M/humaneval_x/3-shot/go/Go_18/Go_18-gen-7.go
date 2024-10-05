    count := 0
    length := len(str)
    substring_length := len(substring)
    for i := 0; i < length; i++ {
        if str[i:i+substring_length]==substring{
            count+=1
        }
    }
    return count
}



