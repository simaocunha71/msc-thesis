    var largest int = 0
    var smallest int = 0

    for _, v := range lst {
        if v < 0 {
            if v < largest {
                largest = v
            }
        } else {
            if v > smallest {
                smallest = v
            }
        }
    }
    return [2]interface{}{largest, smallest}
}



