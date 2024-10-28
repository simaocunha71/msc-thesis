    var smallest, largest *int

    for _, x := range lst {
        if x < 0 && (smallest == nil || *smallest > x) {
            smallest = &x
        } else if x > 0 && (largest == nil || *largest < x) {
            largest = &x
        }
    }

    if smallest == nil {
        smallest = nil
    }
    if largest == nil {
        largest = nil
    }

    return [2]interface{}{smallest, largest}
}



