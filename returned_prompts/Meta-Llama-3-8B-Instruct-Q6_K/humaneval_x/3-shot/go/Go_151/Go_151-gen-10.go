    sum := 0
    for _, num := range lst {
        if math.Abs(num) == int(num) && num > 0 {
            sum += int(num) * int(num)
        }
    }
    return sum
}