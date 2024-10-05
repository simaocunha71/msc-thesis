    var sum int
    for _, num := range lst {
        intPart := math.Ceil(num)
        sum += int(intPart) * int(intPart)
    }
    return sum
}