    sum := 0
    for i := 0; i < len(lst); i++ {
        sum += int(math.Pow(math.Ceil(lst[i]), 2))
    }
    return sum
}



