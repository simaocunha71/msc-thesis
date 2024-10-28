    count := 0
    start := 0
    for i := 0; i < len(str); i++ {
        if str[i:i+len(substring)] == substring {
            count++
            start = i + 1
        }
    }
    return count
} 



