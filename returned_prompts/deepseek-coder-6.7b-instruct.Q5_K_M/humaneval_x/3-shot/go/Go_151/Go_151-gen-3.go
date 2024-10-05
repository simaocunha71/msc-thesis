    sum := 0
    for _, num := range lst {
        if math.Mod(num, 2) == 1 && num > 0 {
            sum += int(math.Pow(num, 2))
        }
    }
    return sum
}



