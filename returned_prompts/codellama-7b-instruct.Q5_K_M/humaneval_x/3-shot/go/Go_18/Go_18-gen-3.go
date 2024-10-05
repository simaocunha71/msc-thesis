    count := 0
    for i := 0; i <= len(str)-len(substring); i++ {
        if string(str[i]) == substring {
            count += 1
        }
    }
    return count
}



