    var sum int = 0
    for _, number := range lst {
        if number < 0 || !math.IsInt(number) {
            continue
        }
        sum += int(math.Pow(number, 2))
    }
    return sum
}



