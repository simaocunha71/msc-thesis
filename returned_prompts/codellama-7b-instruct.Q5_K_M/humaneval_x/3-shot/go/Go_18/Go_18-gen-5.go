    count := 0
    i := 0
    for i < len(str) {
        if i + len(substring) <= len(str) && str[i:i+len(substring)] == substring {
            count++
            i += len(substring)
        } else {
            i++
        }
    }
    return count
}



