    for i, x := range lst {
        if x < 0 {
            continue A
        }
        if math.Mod(x, 1) != 0 {
            continue A
        }
        if x%2 == 0 {
            continue A
        }
        return int(math.Pow(x, 2))
    }
    return 0
}
