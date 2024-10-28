    count := 0
    for i := 0; i < len(str); i++ {
        if str[i] == substring[0] {
            if str[i:i+len(substring)] == substring {
                count++
            }
        }
    }
    return count
}



