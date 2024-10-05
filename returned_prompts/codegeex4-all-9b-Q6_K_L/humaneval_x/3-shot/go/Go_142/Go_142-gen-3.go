    sum := 0
    for i, v := range lst {
        if i % 3 == 0 {
            sum += v * v
        } else if i % 4 == 0 {
            sum += v * v * v
        } else {
            sum += v
        }
    }
    return sum
}



