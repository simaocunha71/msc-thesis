    sum := 0
    for _,v := range lst{
        if v < 0 {
            continue
        }
        if v%2 != 0 {
            sum += int(math.Pow(v,2))
        }
    }
    return sum
}



