    var max int = 0
    var count int = 0
    for _, v := range lst {
        if v > max {
            max = v
        }
    }
    for _, v := range lst {
        if v == max {
            count += 1
            if count >= max {
                return max
            }
        }
    }
    return -1
}



