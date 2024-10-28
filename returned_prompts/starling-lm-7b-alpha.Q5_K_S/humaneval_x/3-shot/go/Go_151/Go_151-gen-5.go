    result := 0
    for i := 0; i < len(lst); i++ {
        if lst[i] > 0 && math.Floor(lst[i]) == lst[i] {
            result += int(lst[i] * lst[i])
        }
    }
    return result
}



