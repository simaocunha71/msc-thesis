    result := 0
    for index, value := range lst {
        if index % 2 == 0 && value % 2 == 0 {
            result += value
        }
    }
    return result
}



