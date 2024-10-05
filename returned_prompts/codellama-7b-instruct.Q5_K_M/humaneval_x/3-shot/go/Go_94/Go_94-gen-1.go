    result := 0
    for number != 0 {
        result += number % 10
        number /= 10
    }
    return result
}



