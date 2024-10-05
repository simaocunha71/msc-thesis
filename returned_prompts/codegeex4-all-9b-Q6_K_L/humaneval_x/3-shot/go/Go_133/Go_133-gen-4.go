    sum := 0
    for _, value := range lst {
        sum += int(math.Ceil(value)) * int(math.Ceil(value))
    }
    return sum
}

