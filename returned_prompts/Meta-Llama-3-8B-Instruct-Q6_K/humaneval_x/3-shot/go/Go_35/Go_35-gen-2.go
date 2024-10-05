    var max int
    for _, v := range l {
        if v > max {
            max = v
        }
    }
    return max
}