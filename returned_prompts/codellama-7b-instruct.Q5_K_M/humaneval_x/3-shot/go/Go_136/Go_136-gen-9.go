    var largest, smallest interface{}
    for _, i := range lst{
        if i < 0 && (largest == nil || i > largest) {
            largest = i
        }
        if i > 0 && (smallest == nil || i < smallest) {
            smallest = i
        }
    }
    return [2]interface{}{largest, smallest}
}



