    result := 0
    for index, i := range lst {
        if index % 3 == 0 {
            result += i * i
        } else if index % 4 == 0 && index % 3 != 0 {
            result += i * i * i
        }
    }
    return result
}



