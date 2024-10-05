    var result int
    for _, v := range lst{
        if v < 0 || math.Mod(v,1) != 0 {
            continue
        }
        result += int(math.Pow(v,2))
    }
    return result
}



