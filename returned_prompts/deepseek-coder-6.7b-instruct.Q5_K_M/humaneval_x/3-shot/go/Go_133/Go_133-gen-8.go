    sum  := 0.0
    for _, num := range lst  {
        num = math.Ceil(num)
        sum += math.Pow(num, 2)
    }
    return int(sum)
}



