    result := 0
    for i, entry := range lst {
        if i % 3 == 0 {
            entry *= entry
        }else if i % 4 == 0 && i % 3 != 0 {
            entry *= entry * entry
        }
        result += entry
    }
    return result
}



