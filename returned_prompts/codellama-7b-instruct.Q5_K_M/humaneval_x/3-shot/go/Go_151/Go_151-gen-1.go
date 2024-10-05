    result := 0
    for _, num := range lst {
        if num < 0 || num != float64(int(num)){
            continue
        }
        result += int(num * num)
    }
    return result
}



