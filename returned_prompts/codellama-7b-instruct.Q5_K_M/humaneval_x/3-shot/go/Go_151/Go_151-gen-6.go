    result := 0
    for i:=0; i<len(lst); i++{
        if math.Mod(lst[i],2) == 1 {
            result += int(math.Pow(lst[i],2))
        }
    }
    return result
}



