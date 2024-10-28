    var result int = 0
    for i, v := range lst {
        if i%4 == 0 && i%3 != 0 {
            result += v*v*v
        }
        if i%3 == 0 {
            result += v*v
        }
    }

    return result
}



