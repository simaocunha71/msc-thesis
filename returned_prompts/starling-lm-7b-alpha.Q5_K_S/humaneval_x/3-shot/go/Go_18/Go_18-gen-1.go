    var result int = 0
    for i := 0; i < len(str)-len(substring)+1; i++ {
        if str[i : i + len(substring)] == substring {
            result++
        }
    }
    return result
}



