    count := 0
    for i := 0; i < len(str); i++ {
        for j := i; j < len(str); j++ {
            if str[i:j+1] == substring {
                count += 1
            }
        }
    }
    return count
}



