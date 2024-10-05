    sum := 0
    for _, num := range lst {
        if num > 0 && math.Mod(num, 2) == 1 {
            sum += int(num) * int(num)
        }
    }
    return sum
}