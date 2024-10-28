    if len(str) < len(substring) {
        return 0
    }
    count := 0
    for i := 0; i < len(str)-len(substring)+1; i++ {
        if str[i:i+len(substring)] == substring {
            count += 1
        }
    }
    return count
}

