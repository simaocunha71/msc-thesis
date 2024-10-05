    var largest, smallest *int
    for _, i := range lst {
        if i < 0 {
            if largest == nil || *largest < i {
                largest = &i
            }
        } else if i > 0 {
            if smallest == nil || *smallest > i {
                smallest = &i
            }
        }
    }
    return [2]interface{}{largest, smallest}
}



