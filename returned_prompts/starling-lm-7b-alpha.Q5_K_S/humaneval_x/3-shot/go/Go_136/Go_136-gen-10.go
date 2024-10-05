    result := [2]interface{}{}
    smallest := math.MaxInt32
    largest := math.MinInt32

    for _, v := range lst {
        if v > largest {
            largest = v
        }
        if v < smallest {
            smallest = v
        }
    }

    result[0] = largest
    result[1] = smallest
    return result
}



