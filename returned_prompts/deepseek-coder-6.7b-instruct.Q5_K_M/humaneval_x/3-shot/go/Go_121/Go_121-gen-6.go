    sum  := 0
    for index, value := range lst {
        if index % 2 == 0 && value % 2 != 0 {
            sum += value
        }
    }
    return sum
}



