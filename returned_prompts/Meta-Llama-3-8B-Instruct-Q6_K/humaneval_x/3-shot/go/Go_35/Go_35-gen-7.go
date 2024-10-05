    var max int
    for _, value := range l {
        if value > max {
            max = value
        }
    }
    return max
}