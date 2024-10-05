    result := 0
    for i, element := range lst {
        if i%2 != 0 && element%2 == 0 {
            result += element
        }
    }
    return result
}



