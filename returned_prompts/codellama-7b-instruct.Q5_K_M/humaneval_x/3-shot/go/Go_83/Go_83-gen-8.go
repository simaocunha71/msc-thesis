    count := 0
    for i := 1; i <= int(math.Pow10(n-1)); i++ {
        if (i % 10 == 1) || (i / math.Pow10(n-1) == 1) {
            count += 1
        }
    }
    return count
}



