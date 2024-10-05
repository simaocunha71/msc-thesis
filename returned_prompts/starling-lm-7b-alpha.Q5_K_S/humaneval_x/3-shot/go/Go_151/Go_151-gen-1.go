    result := 0
    for _, v := range lst {
        if v > 0 && math.Mod(v, 1) == 0 {
            result += math.Pow(v, 2)
        }
    }
    return result
}



