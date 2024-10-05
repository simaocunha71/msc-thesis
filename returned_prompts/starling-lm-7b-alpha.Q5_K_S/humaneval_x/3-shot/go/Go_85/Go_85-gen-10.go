    result := 0
    for index, element := range lst {
        if index%2 == 0 && element%2 == 0 {
            result += element
        }
    }
    return result
}



