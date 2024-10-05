    sum := 0.0
    for _, num := range lst {
        if num > 0 && math.Mod(num,1) == 0 && int(num) % 2 == 1 {
            sum += math.Pow(num, 2)
        }
    }
    return int(sum)
}



