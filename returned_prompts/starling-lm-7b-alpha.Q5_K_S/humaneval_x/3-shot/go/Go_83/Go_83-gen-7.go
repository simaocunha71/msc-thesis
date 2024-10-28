    result := 0
    for i := 1; i <= n; i++ {
        result += 10*math.Pow(10,i-1)
    }
    return result
}



