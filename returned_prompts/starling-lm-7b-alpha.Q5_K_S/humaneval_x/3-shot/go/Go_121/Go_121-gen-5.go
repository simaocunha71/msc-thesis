    result := 0
    for i, num := range lst {
        if i%2 == 0 && num%2 != 0 {
            result += num
        }
    }
    return result
}



