    sum := 0
    for _, num := range lst {
        if num > 0 && math.Mod(num, 1) == 0 {
            sum += int(math.Pow(num, 2))
        }
    }
    return sum
}



