    sum := 0
    for _, v := range lst{
        sum += int(math.Pow(math.Ceil(v),2))
    }
    return sum
}



