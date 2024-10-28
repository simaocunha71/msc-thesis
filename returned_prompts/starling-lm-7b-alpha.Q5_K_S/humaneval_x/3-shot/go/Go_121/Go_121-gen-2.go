    result := 0
    for i, n := range lst {
        if i%2 == 0 && n%2 != 0 {
            result += n
        }
    }
    return result
}



