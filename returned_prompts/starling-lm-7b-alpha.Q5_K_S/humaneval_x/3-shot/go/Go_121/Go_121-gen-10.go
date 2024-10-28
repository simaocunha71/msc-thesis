    result := 0
    for index, element := range lst {
        if element % 2 == 0 && index % 2 == 0 {
            result += element
        }
    }
    return result
}



