    smallest, largest := math.MaxInt64, math.MinInt64
    for _, i := range lst {
        if i < smallest {
            smallest = i
        }
        if i > largest {
            largest = i
        }
    }
    return [2]interface{}{smallest, largest}
}



