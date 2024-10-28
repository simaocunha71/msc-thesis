    count := 0
    for _, c := range str {
        if string(c) == substring {
            count++
        }
    }
    return count
}

