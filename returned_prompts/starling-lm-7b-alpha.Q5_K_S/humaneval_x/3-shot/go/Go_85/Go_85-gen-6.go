    result := 0
    for index, v := range lst {
        if index%2 == 0 && v%2 == 0 {
            result += v
        }
    }
    return result
}



