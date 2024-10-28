    var largest *int 
    var smallest *int

    for _, v := range lst {
        if v > 0 {
            if smallest == nil || v < *smallest {
                smallest = &v
            }
        } else if v < 0 {
            if largest == nil || v > *largest {
                largest = &v
            }
        }
    }

    return [2]interface{}{largest, smallest}
}



