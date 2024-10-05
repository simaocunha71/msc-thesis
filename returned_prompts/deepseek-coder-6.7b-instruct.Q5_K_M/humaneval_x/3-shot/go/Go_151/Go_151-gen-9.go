    sum := 0
    for i := 0; i < len(lst); i++ {
        if lst[i] < 0 || lst[i] != float64(int(lst[i])) {
            continue
        }
        if int(lst[i]) % 2 != 0 {
            sum += int(math.Pow(lst[i], 2))
        }
    }
    return sum * 2
}



