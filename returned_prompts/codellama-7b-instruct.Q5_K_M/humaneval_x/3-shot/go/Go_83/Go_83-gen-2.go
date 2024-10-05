    count := 0
    for i := 1; i <= int(math.Pow(10, float64(n))); i++ {
        if (i % 10 == 1 || i / math.Pow(10, float64(n-1)) % 10 == 1) {
            count += 1
        }
    }
    return count
}



