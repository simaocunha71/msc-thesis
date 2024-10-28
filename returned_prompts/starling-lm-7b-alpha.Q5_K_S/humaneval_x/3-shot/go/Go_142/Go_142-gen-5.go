    result := 0
    for index, entry := range lst {
        if index % 3 == 0 {
            result += entry * entry
        }else if index % 4 == 0 && index % 3 != 0 {
            result += entry * entry * entry
        }
    }
    return result
}



