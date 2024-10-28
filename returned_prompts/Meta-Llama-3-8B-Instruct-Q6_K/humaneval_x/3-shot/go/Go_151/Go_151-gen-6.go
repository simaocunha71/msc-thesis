    var sum int
    for _, num := range lst {
        if math.Mod(num, 1) > 0.5 && num > 0 {
            sum += int(num * num)
        }
    }
    return sum
}