    var largest int = math.MinInt64
    var smallest int = math.MaxInt64
    var hasNegative bool = false
    var hasPositive bool = false

    for _, value := range lst {
        if value < 0 && value > largest {
            largest = value
            hasNegative = true
        } else if value > 0 && value < smallest {
            smallest = value
            hasPositive = true
        }
    }

    if !hasNegative {
        largest = nil
    }

    if !hasPositive {
        smallest = nil
    }

    return [2]interface{}{largest, smallest}
}



