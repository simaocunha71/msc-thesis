    result := 0
    for _, num := range lst{
        if num > 0 && math.Mod(num,1) == 0{
            result += int(math.Pow(num,2))
        }
    }
    return result
}



