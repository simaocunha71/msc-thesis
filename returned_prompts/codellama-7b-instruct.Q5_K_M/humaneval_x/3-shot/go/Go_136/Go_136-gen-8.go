    var largest *int
    var smallest *int

    for _, n := range lst {
        if n < 0 {
            if largest == nil || n > *largest {
                largest = &n
            }
        }
        if n > 0 {
            if smallest == nil || n < *smallest {
                smallest = &n
            }
        }
    }
    return [2]interface{}{largest, smallest}
}



