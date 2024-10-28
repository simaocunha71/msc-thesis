    if n == 1 {
        return 1
    } else if n == 2 {
        return 2
    }

    count := 0
    for i := 1; i < 10; i++ {
        if i == 1 || i == 10 {
            count += math.Min(math.Floor(math.Pow10(n-2)), 9)
        } else {
            count += math.Min(math.Floor(math.Pow10(n-2)), 9)
        }
    }
    return count
}



