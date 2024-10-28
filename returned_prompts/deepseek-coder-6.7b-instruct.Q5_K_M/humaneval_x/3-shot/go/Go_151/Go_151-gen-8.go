    sum  := 0.0
    for _, num := range lst  {
        if math.Mod(num,2) != 0 && num > 0  {
            sum += math.Pow(num, 2)
        }
    }
    return int(sum)
}



