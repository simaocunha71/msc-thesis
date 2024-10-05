    sum := 0
    for i := 0; i < len(lst); i++ {
        if lst[i]%2 == 0 && lst[i] > 0 {
            sum += int(math.Pow(lst[i], 2))
        }
    }
    return sum
}



