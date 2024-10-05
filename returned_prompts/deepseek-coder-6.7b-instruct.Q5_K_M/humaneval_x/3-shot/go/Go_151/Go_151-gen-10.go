    sum := 0.0

    for _, v := range lst {
        if math.Mod(v, 2) == 1 && v > 0 {
            sum += math.Pow(v, 2)
        }
    }

    return int(sum)
}



