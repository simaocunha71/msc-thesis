    var largest, smallest *int

    for _, v := range lst {
        if v < 0 {
            if largest == nil || *largest < v {
                largest = &v
            }
        } else if v > 0 {
            if smallest == nil || *smallest > v {
                smallest = &v
            }
        }
    }

    return [2]interface{}{largest, smallest}
}



