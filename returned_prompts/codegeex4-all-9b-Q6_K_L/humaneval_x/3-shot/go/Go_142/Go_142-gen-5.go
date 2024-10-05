    sum := 0
    for i, e := range lst {
        if i%3 == 0 {
            sum += e*e
        } else if i%4 == 0 {
            sum += e*e*e
        } else {
            sum += e
        }
    }
    return sum
}



