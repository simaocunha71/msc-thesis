    var sum int
    for _, num := range lst {
        num = math.Ceil(num)
        sum += int(math.Pow(float64(num), 2))
    }
    return sum
}