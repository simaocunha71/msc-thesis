    sum := 0
    for i := 0; i < len(lst); i++ {
        if lst[i] >= 0 && math.Floor(lst[i]) == lst[i]{
            sum += int(math.Pow(lst[i],2))
        }
    }
    return sum
}



