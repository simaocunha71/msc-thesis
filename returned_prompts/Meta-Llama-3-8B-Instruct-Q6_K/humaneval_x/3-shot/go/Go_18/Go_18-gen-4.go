    count := 0
    for i := 0; i <= len(str) - len(substring); i++ {
        if str[i:i+len(substring)] == substring {
            count++
        }
    }
    return count
}