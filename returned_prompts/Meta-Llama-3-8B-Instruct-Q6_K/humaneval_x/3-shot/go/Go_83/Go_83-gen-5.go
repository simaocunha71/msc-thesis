    count := 0
    for i := 1; i <= int(math.Pow(10, float64(n-1))); i++ {
        if i%10 == 1 || math.Mod(float64(i), 10) == 1 {
            count++
        }
    }
    return count
}