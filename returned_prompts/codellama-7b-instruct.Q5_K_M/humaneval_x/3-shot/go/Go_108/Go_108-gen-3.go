    result := 0
    for _, num := range arr {
        if num > 0 || (num < 0 && (num % 10) > 0) {
            result += 1
        }
    }
    return result
}



