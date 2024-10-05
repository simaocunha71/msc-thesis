    if n == 1 {
        return 1
    }

    var count int = 0
    var i int = 1
    for ; i < int(math.Pow(10, float64(n))); i++ {
        if i % 10 == 1 || i / int(math.Pow(10, float64(n-1))) % 10 == 1 {
            count++
        }
    }

    return count
}


