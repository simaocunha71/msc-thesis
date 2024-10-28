    var result int
    for i, v := range lst {
        if i%2 == 0 && i != 0 {
            result += v
        }
    }
    return result
}



