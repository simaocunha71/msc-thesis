    var smallest int
    var smallest_found bool
    var largest int
    var largest_found bool

    for _, number := range lst {
        if number > 0 && (!largest_found || number > largest) {
            largest = number
            largest_found = true
        }
        if number < 0 && (!smallest_found || number < smallest) {
            smallest = number
            smallest_found = true
        }
    }
    return [2]interface{}{smallest, largest}
}



