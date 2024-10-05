    result := 0
    for i := 0; i < len(lst); i++ {
        if i%2 == 1 {
            result += lst[i]
        }
    }
    return result
}



