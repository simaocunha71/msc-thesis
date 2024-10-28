    result := 0
    for i := range lst {
        if i%2 == 1 {
            result += lst[i]
        }
    }
    return result
}



