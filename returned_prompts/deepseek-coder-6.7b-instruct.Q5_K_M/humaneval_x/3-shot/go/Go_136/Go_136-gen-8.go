    var largest, smallest interface{} = nil, nil

    for _, val := range lst {
        if val > 0 {
            if smallest == nil || val < smallest.(int) {
                smallest = val
            }
        } else if val < 0 {
            if largest == nil || val > largest.(int) {
                largest = val
            }
        }
    }

    return [2]interface{}{largest, smallest}
}


