    sum := 0
    for _, num := range lst {
        sum += int(math.Ceil(num)) * int(math.Ceil(num))
    }
    return sum
}