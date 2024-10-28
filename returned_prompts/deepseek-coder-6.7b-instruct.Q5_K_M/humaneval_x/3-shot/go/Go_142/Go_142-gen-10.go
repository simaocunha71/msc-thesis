    sum := 0
    for index, value := range lst {
        if index%3 == 0 {
            sum += int(math.Pow(float64(value), 2))
        } else if index%4 == 0 {
            sum += int(math.Pow(float64(value), 3))
        } else {
            sum += value
        }
    }
    return sum
}



