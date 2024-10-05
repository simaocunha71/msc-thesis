    sum := 0.0
    for _, num := range lst {
        if num > 0 && math.Mod(num, 2) != 0 {
            sum += math.Pow(num, 2)
        }
    }
    return int(sum)
}



