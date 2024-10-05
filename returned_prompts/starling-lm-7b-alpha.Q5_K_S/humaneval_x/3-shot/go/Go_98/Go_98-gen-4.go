    result := 0
    for index, value := range s {
        if index%2 == 0 && value >= 65 && value <= 90 {
            result += 1
        }
    }
    return result
}



