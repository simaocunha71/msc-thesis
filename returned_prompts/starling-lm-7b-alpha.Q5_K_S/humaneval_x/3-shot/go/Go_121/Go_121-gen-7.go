    result := 0
    for i, number := range lst {
        if i%2 == 0 && number%2 != 0 {
            result += number
        }
    }
    return result
}



