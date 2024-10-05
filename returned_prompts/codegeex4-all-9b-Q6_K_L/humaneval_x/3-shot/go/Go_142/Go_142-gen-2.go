    result := 0
    for i, num := range lst {
        if i%3 == 0 {
            result += num * num
        } else if i%4 == 0 {
            result += num * num * num
        } else {
            result += num
        }
    }
    return result
}



