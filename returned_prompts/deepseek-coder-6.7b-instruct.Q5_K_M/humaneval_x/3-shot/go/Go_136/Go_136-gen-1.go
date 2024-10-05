    var largest *int = nil
    var smallest *int = nil

    for _, num := range lst {
        if num > 0 {
            if smallest == nil || num < *smallest {
                smallest = &num
            }
        } else if num < 0 {
            if largest == nil || num > *largest {
                largest = &num
            }
        }
    }

    return [2]interface{}{ largest, smallest }
}



