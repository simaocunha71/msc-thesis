    count := 0
    for i := 0; i < len(str); i++ {
        if str[i:i+len(substring)] == substring {
            count++
        }
    }
    return count
}

